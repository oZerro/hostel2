from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

from otchet.models import (
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


class InfoUserForm(forms.Form):
    room_number = forms.IntegerField(
        label="Номер комнаты",
        max_value=17,
        min_value=2,
        error_messages={
            'max_value': 'Слишком большой номер, всего 17 комнат',
            'min_value': 'Номера начинаются с 2',
            'required': 'Укажите номер'
        })
    phone = forms.CharField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'password1', 'password2')


# class AddPepForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=100, min_length=2, error_messages={
#         'required': 'Поле не должно быть пустым',
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов'
#     })
#     balanсe = forms.IntegerField(label='Баланс')
#     room = forms.ChoiceField(label='Номер комнаты', max_length=2)
#     phone_number = forms.CharField(label='Номер телефона', max_length=11, initial="79876543412")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class AddPepForm(forms.ModelForm):
    phone_number = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '79876543412'}),
    )

    class Meta:
        model = Profile
        fields = ('name', 'room', 'phone_number')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departures
        fields = ('user',)


class AddPaymentsForm(forms.ModelForm):
    summa = forms.IntegerField(
        label='Сумма',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '0'}),
    )

    class Meta:
        model = Payments
        fields = ('user', 'method', 'summa')


class AddSpendingAdminForm(forms.ModelForm):
    summa = forms.IntegerField(
        label='Сумма',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '0'}),
    )

    class Meta:
        model = SpendingAdmin
        fields = '__all__'


class AddSpendingHostelForms(forms.ModelForm):
    summa = forms.IntegerField(
        label='Сумма',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '0'}),
    )

    class Meta:
        model = SpendingHostel
        fields = '__all__'


class AddSpendingBossForms(forms.ModelForm):
    summa = forms.IntegerField(
        label='Сумма',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '0'}),
    )

    class Meta:
        model = SpendingBoss
        fields = '__all__'


class AddEventsForms(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'


class AddRefundsForms(forms.ModelForm):
    summa = forms.IntegerField(
        label='Сумма',
        widget=forms.TextInput(attrs={'onfocus': "this.value=''", 'value': '0'}),
    )

    class Meta:
        model = Refunds
        fields = ('user', 'method', 'summa')
