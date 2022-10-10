from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from rest_framework import generics

from .funk_otchet import (
    data_d,
    add_paginator,
    summ_room,
    point_in_number,
    suum_vsego,
    spend_vsego,
    spending_for_month,
    dict_from_list_room,
    count_new_people,
    arrivals_departures,
    add_refaunds,
    add_payments,
    add_customer,
    add_department,
    count_month_number,
    otchet_data,
    send,
)
from .forms import (
    InfoUserForm,
    UserLoginForm,
    UserRegisterForm,
    AddPepForm,
    DepartmentForm,
    AddPaymentsForm,
    AddSpendingAdminForm,
    AddSpendingHostelForms,
    AddSpendingBossForms,
    AddEventsForms,
    AddRefundsForms,
    AddRoomForm,
    ContactForm,
)

from .models import (
    Profile,
    Room,
    Departures,
    Payments,
    Refunds,
    SpendingAdmin,
    SpendingBoss,
    SpendingHostel,
    Events,
    Contact,
)

from .serializers import ProfileSerializer
from .tasks import send_spam_send


class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


form_names = {
    "AddEventsForms":  AddEventsForms,
    "AddPepForm": AddPepForm,
    "AddPaymentsForm": AddPaymentsForm,
    "AddSpendingAdminForm": AddSpendingAdminForm,
    "AddSpendingHostelForms": AddSpendingHostelForms,
    "AddSpendingBossForms": AddSpendingBossForms,
    "DepartmentForm": DepartmentForm,
    "AddRefundsForms": AddRefundsForms,
    "AddRoomForm": AddRoomForm,
}

form_names_individ = [
    "AddPepForm",
    "AddPaymentsForm",
    "AddRefundsForms",
    "DepartmentForm",
]


def index(request):
    data = data_d(request)
    if request.method == 'POST':
        data['new'] = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        form_new = data['new']
        if form_new.is_valid():
            if name_form not in form_names_individ:
                form_new.save()
                return redirect('index')

            elif name_form == form_names_individ[0]:  # добавление посетителя
                if not add_customer(form_new):
                    messages.error(
                        request, f"{form_new.cleaned_data['room'].__str__()} занята, укажите другую"
                    )
                    return render(request, 'otchet/index.html', context=data)
                else:
                    return render(request, 'otchet/index.html', context=data)
            elif name_form == form_names_individ[1]:  # добавление платежа
                add_payments(form_new)
                return redirect('index')
            elif name_form == form_names_individ[2]:  # добавить возврата
                add_refaunds(form_new)
                return redirect('index')
            elif name_form == form_names_individ[3]:  # добавление выселения
                add_department(form_new)
                return redirect('index')
    else:
        return render(request, 'otchet/index.html', context=data)


def rooms(request):
    data = add_paginator(request, Room)
    data['rooms'] = Room.objects.all()

    vsego_mest = 0
    for col_vo in data['rooms']:
        vsego_mest += col_vo.number_of_beds

    data['vsego_mest'] = vsego_mest

    if request.method == 'POST':
        form = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form.is_valid():
            if name_form not in form_names_individ:
                form.save()
                return redirect('rooms')

    return render(request, 'otchet/rooms.html', context=data)


def update_rooms(request, id_room):
    data = data_d(request)
    pay = get_object_or_404(Room, id=id_room)

    if request.method == 'POST' and request.POST['name_form'] == 'AddRoomForm':
        form1 = AddRoomForm(data=request.POST, instance=pay)
        data['form8'] = form1
        if form1.is_valid():
            form1.save()
            return redirect('rooms')
    else:
        form1 = AddRoomForm(instance=pay)
        data['form8'] = form1
    return render(request, 'otchet/update_room.html', context=data)


def delete_rooms(request, id_room):
    room = get_object_or_404(Room, id=id_room)
    room.delete()
    return redirect('rooms')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'otchet/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'otchet/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def otchet(request):
    data = otchet_data(request)

    return render(request, 'otchet/otchet.html', context=data)

#-------------------------------------------------------------
def payments(request):
    data = add_paginator(request, Payments)

    if request.method == 'POST':
        form_f = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form_f.is_valid():
            if name_form == form_names_individ[1]:  # добавление платежа
                add_payments(form_f)
                return redirect('payments')
            elif name_form == form_names_individ[2]:  # добавить возврата
                add_refaunds(form_f)
        return render(request, 'otchet/payments.html', context=data)
    else:
        return render(request, 'otchet/payments.html', context=data)


def update_payments(request, id_pay):
    data = data_d(request)
    pay = get_object_or_404(Payments, id=id_pay)

    if request.method == 'POST' and request.POST['name_form'] == 'AddPaymentsForm':
        form1 = AddPaymentsForm(data=request.POST, instance=pay)
        data['form1'] = form1
        if form1.is_valid():
            form1.save()
            return render(request, 'otchet/done.html', context=data)
    else:
        form1 = AddPaymentsForm(instance=pay)
        data['form1'] = form1
    return render(request, 'otchet/update_payments.html', context=data)


def delete_payments(request, id_pay):
    pay = get_object_or_404(Payments, id=id_pay)
    pay.delete()
    return redirect('payments')

#-------------------------------------------------------------
def peoples(request):
    data = add_paginator(request, Profile)

    if request.method == 'POST':
        form_f = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')

        if form_f.is_valid():

            if name_form == form_names_individ[0]:  # добавление жильца
                if not add_customer(form_f):
                    messages.error(
                        request, f"{form_f.cleaned_data['room'].__str__()} занята, укажите другую"
                    )
                    return render(request, 'otchet/people.html', context=data)
                else:
                    return redirect('peoples')

            elif name_form == form_names_individ[3]:  # добавить выселение
                add_department(form_f)
                return redirect('peoples')
        return render(request, 'otchet/people.html', context=data)
    else:
        return render(request, 'otchet/people.html', context=data)


def update_peoples(request, id_people):
    data = data_d(request)
    people = get_object_or_404(Profile ,id=id_people)

    if request.method == 'POST' and request.POST['name_form'] == 'AddPepForm':
        form = AddPepForm(data=request.POST, instance=people)
        data['form'] = form
        if form.is_valid():
            if form.cleaned_data['room'].is_full:
                messages.error(
                    request, f"{form.cleaned_data['room'].__str__()} занята, укажите другую"
                )
                return render(request, 'otchet/index.html', context=data)
            else:
                form.save()
                return render(request, 'otchet/done.html', context=data)
    else:
        form = AddPepForm(instance=people)
        data['form'] = form
    return render(request, 'otchet/update_peoples.html', context=data)


def delete_peoples(request, id_people):
    people = get_object_or_404(Profile, id=id_people)
    people.delete()
    return redirect('peoples')


#-------------------------------------------------------------
def spendinghostel(request):
    data = add_paginator(request, SpendingHostel)

    if request.method == 'POST':
        form = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form.is_valid():
            if name_form not in form_names_individ:
                form.save()
                return redirect('spendinghostel')

    return render(request, 'otchet/spending_hostel.html', context=data)


def update_spendinghostel(request, id_spend):
    data = data_d(request)
    spend = get_object_or_404(SpendingHostel, id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingHostelForms':
        form3 = AddSpendingHostelForms(data=request.POST, instance=spend)
        data['form3'] = form3
        if form3.is_valid():
            form3.save()
            return redirect('spendinghostel')
    else:
        form3 = AddSpendingHostelForms(instance=spend)
        data['form3'] = form3
    return render(request, 'otchet/updadte_spending_hostel.html', context=data)


def delete_spendinghostel(request, id_spend):
    spend = get_object_or_404(SpendingHostel, id=id_spend)
    spend.delete()
    return redirect('spendinghostel')
#-------------------------------------------------------------

def spendingadmin(request):
    data = add_paginator(request, SpendingAdmin)

    if request.method == 'POST':
        form = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form.is_valid():
            if name_form not in form_names_individ:
                form.save()
                return redirect('spendingadmin')

    return render(request, 'otchet/spending_admin.html', context=data)


def update_spendingadmin(request, id_spend):
    data = data_d(request)
    spend = get_object_or_404(SpendingAdmin, id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingAdminForm':
        form2 = AddSpendingAdminForm(data=request.POST, instance=spend)
        data['form2'] = form2
        if form2.is_valid():
            form2.save()
            return redirect('spendingadmin')
    else:
        form2 = AddSpendingAdminForm(instance=spend)
        data['form2'] = form2
    return render(request, 'otchet/update_spend_admin.html', context=data)


def delete_spendingadmin(request, id_spend):
    spend = get_object_or_404(SpendingAdmin, id=id_spend)
    spend.delete()
    return redirect('spendingadmin')

def spendingboss(request):
    data = add_paginator(request, SpendingBoss)

    if request.method == 'POST':
        form = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form.is_valid():
            if name_form not in form_names_individ:
                form.save()
                return redirect('spendingboss')

    return render(request, 'otchet/spending_boss.html', context=data)

def update_spendingboss(request, id_spend):
    data = data_d(request)
    spend = get_object_or_404(SpendingBoss, id=id_spend)

    if request.method == 'POST' and request.POST['name_form'] == 'AddSpendingBossForms':
        form4 = AddSpendingBossForms(request.POST, instance=spend)
        if form4.is_valid():
            form4.save()
            return redirect('spendingboss')
    else:
        form4 = AddSpendingBossForms(instance=spend)
        data['form4'] = form4
    return render(request, 'otchet/update_spending_boss.html', context=data)

def delete_spendingboss(request, id_spend):
    spend = get_object_or_404(SpendingBoss, id=id_spend)
    spend.delete()
    return redirect('spendingboss')


def events(request):
    data = add_paginator(request, Events)

    if request.method == 'POST':
        form = form_names[request.POST.get('name_form')](request.POST)
        name_form = request.POST.get('name_form')
        if form.is_valid():
            if name_form not in form_names_individ:
                form.save()
                return redirect('events')
    return render(request, 'otchet/events.html', context=data)


def update_events(request, id_event):
    data = data_d(request)
    event = get_object_or_404(Events, id=id_event)

    if request.method == 'POST' and request.POST['name_form'] == 'AddEventsForms':
        form5 = AddEventsForms(request.POST, instance=event)
        if form5.is_valid():
            form5.save()
            return redirect('events')
    else:
        form5 = AddEventsForms(instance=event)
        data['form5'] = form5
    return render(request, 'otchet/update_event.html', context=data)


def delete_events(request, id_event):
    event = get_object_or_404(Events, id=id_event)
    event.delete()
    return redirect('events')


def test(request):
    form_class = ContactForm

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            send(contact.instance.email, contact.instance.name)
            # send_spam_send.delay(contact.instance.email, contact.instance.name)
            return render(request, 'otchet/done.html', context={'qwer': "привет"})

    return render(request, 'otchet/test.html', context={'form_test': form_class})


