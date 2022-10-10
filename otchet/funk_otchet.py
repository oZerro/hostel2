from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.mail import send_mail
import datetime

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
)


def send(user_email, name):
    send_mail(
        'Здарова',
        f'Здарова, {name}',
        'leha.normatov@mail.ru',
        [user_email, ],
        fail_silently=False,
    )


def data_d(request) -> dict:
    data = {}
    if request.user.is_authenticated and request.user.is_staff:
        name = request.user.first_name
        surname = request.user.last_name
        payments = list(Payments.objects.all())[:5]
        data = {
            'name': name,
            'surname': surname,
            'payments': payments
        }

    elif request.user.is_authenticated:
        name = request.user.first_name
        surname = request.user.last_name
        data = {
            'name': name,
            'surname': surname
        }

    data['form'] = AddPepForm()
    data['form1'] = AddPaymentsForm()
    data['form2'] = AddSpendingAdminForm()
    data['form3'] = AddSpendingHostelForms()
    data['form4'] = AddSpendingBossForms()
    data['form5'] = AddEventsForms()
    data['form6'] = AddRefundsForms()
    data['form7'] = DepartmentForm()
    data['form8'] = AddRoomForm()

    return data


def add_paginator(request, obj_model) -> dict:
    data = data_d(request)
    objects_all = obj_model.objects.all()
    paginator = Paginator(objects_all, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return data

def summ_room(number) -> str:
    arr_suum = []
    for pay in Payments.objects.all():
        if (
                int(pay.room) == number and
                datetime.datetime.now().month == pay.date.month
        ):
            arr_suum.append(pay.summa)
    return point_in_number(sum(arr_suum))

def point_in_number(arr) -> str:  # расставляет точки в больших числах
    if arr < 0:
        s = list(str(arr)[1:])
    else:
        s = list(str(arr))

    count = 0
    i = 0
    while i < len(s) - 1:
        count += 1
        i += 1
        if count == 3:
            s.insert(len(s) - i, '.')
            count = 0
            i += 1
    if arr < 0:
        return "-" + "".join(s)
    else:
        return "".join(s)

def suum_vsego() -> tuple:
    arr_suum = []
    for pay in Payments.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_suum.append(pay.summa)
    summa = sum(arr_suum)

    return point_in_number(summa), sum(arr_suum)


def spend_vsego(r) -> tuple:
    arr_suum = []
    for pay in r.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_suum.append(pay.summa)
    summa = sum(arr_suum)

    return point_in_number(summa), sum(arr_suum)


def spending_for_month(s) -> list:
    arr_spend = []
    for pay in s.objects.all():
        if datetime.datetime.now().month == pay.date.month:
            arr_spend.append(pay)
    return arr_spend


def dict_from_list_room(arrivals) -> dict:
    new_people_room = {}
    while len(arrivals) > 0:
        com = arrivals[0]
        x = arrivals.count(com)
        new_people_room[com] = x
        if x > 0:
            while x > 0:
                arrivals.remove(com)
                x -= 1

    return new_people_room


def count_new_people() -> tuple:
    summ = 0

    arrivals = []  # заезды
    for profile in Profile.objects.all():
        if profile.date.month == datetime.datetime.now().month:
            if profile.room:
                arrivals.append(profile.room.number)

    for people in Profile.objects.all():
        if datetime.datetime.now().month == people.date.month:
            summ += 1

    return summ, dict_from_list_room(arrivals)


def arrivals_departures() -> tuple:
    summ = 0

    arrivals = []  # выезды
    for profile in Departures.objects.all():
        if profile.date.month == datetime.datetime.now().month:
            arrivals.append(profile.room)

    for people in Departures.objects.all():
        if datetime.datetime.now().month == people.date.month:
            summ += 1

    return summ, dict_from_list_room(arrivals)


def add_refaunds(form) -> None:
    if form.cleaned_data['summa'] > 0:
        pay = Payments(
            user=form.cleaned_data['user'],
            method=form.cleaned_data['method'],
            name=form.cleaned_data['user'].name,
            summa=form.cleaned_data['summa'] * (-1),
            room=form.cleaned_data['user'].room.number
        )
        pay.save()

        refa = Refunds(
            user=form.cleaned_data['user'],
            method=form.cleaned_data['method'],
            name=form.cleaned_data['user'].name,
            summa=form.cleaned_data['summa'] * (-1),
            room=form.cleaned_data['user'].room.number
        )
        refa.save()
    else:
        pay = Payments(
            user=form.cleaned_data['user'],
            method=form.cleaned_data['method'],
            name=form.cleaned_data['user'].name,
             summa=form.cleaned_data['summa'],
            room=form.cleaned_data['user'].room.number
        )
        pay.save()

        refa = Refunds(
            user=form.cleaned_data['user'],
            method=form.cleaned_data['method'],
            name=form.cleaned_data['user'].name,
            summa=form.cleaned_data['summa'],
            room=form.cleaned_data['user'].room.number
        )
        refa.save()


def add_payments(form) -> bool:
    pay = Payments(
        user=form.cleaned_data['user'],
        method=form.cleaned_data['method'],
        name=form.cleaned_data['user'].name,
        summa=form.cleaned_data['summa'],
        room=form.cleaned_data['user'].room.number

    )
    pay.save()

    return True


def add_customer(form) -> bool:
    if form.cleaned_data['room'].is_full:
        return False
    else:
        profile = Profile(
            name=form.cleaned_data['name'],
            phone_number=form.cleaned_data['phone_number'],
            room=form.cleaned_data['room'],
            room_number=form.cleaned_data['room'].number
        )
        profile.save()
        return True


def add_department(form) -> bool:
    if form.is_valid():
        user_id = form.cleaned_data['user'].id
        user_none = Profile.objects.get(id=user_id)
        depart = Departures(
            name=form.cleaned_data['user'].name,
            phone_number=form.cleaned_data['user'].phone_number,
            room=form.cleaned_data['user'].room.number
        )
        user_none.delete()
        depart.save()
    return True

def count_month_number() -> str:
    if datetime.datetime.now().month < 10:
        month_now = '0' + str(datetime.datetime.now().month)
    else:
        month_now = datetime.datetime.now().month

    return str(month_now)


def otchet_data(request) -> dict:
    data = data_d(request)

    month_next = int(count_month_number()) + 1

    data['month_now'] = count_month_number()
    data['month_next'] = month_next

    data['summ_2_room'] = summ_room(2)
    data['summ_3_room'] = summ_room(3)
    data['summ_4_room'] = summ_room(4)
    data['summ_5_room'] = summ_room(5)
    data['summ_6_room'] = summ_room(6)
    data['summ_10_room'] = summ_room(10)
    data['summ_11_room'] = summ_room(11)
    data['summ_12_room'] = summ_room(12)
    data['summ_13_room'] = summ_room(13)
    data['summ_14_room'] = summ_room(14)
    data['summ_15_room'] = summ_room(15)
    data['summ_16_room'] = summ_room(16)
    data['summ_17_room'] = summ_room(17)
    data['suum_vsego'] = suum_vsego()[0]
    data['spending_boss'] = spending_for_month(SpendingBoss)
    data['spend_vsego_boss'] = spend_vsego(SpendingBoss)[0]
    data['spending_dom'] = spending_for_month(SpendingHostel)
    data['spend_vsego_dom'] = spend_vsego(SpendingHostel)[0]
    data['count_new_people'] = count_new_people()
    data['count_depart_people'] = arrivals_departures()
    data['events'] = list(Events.objects.all())
    data['spend_admin'] = spend_vsego(SpendingAdmin)[0]
    data['banca'] = point_in_number((
            suum_vsego()[1] -
            (
                    spend_vsego(SpendingBoss)[1] +
                    spend_vsego(SpendingHostel)[1] +
                    spend_vsego(SpendingAdmin)[1]
            )
    ))

    return data



