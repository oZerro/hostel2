# Generated by Django 4.0.5 on 2022-07-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, null=True, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=20, null=True, verbose_name='Номер телефона')),
                ('balance', models.IntegerField(default=0, verbose_name='Баланс')),
                ('other_day', models.PositiveSmallIntegerField(default=0, verbose_name='Остаток дней')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=0, verbose_name='Номер комнаты')),
                ('price_for_period', models.IntegerField(default=7000, verbose_name='Стоимость')),
                ('number_of_beds', models.PositiveSmallIntegerField(default=1, verbose_name='Количество мест')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('summa', models.PositiveIntegerField(default=0, verbose_name='Сумма')),
                ('note', models.CharField(max_length=200, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingBoss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('summa', models.PositiveIntegerField(default=0, verbose_name='Сумма')),
                ('note', models.CharField(max_length=200, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingHostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('summa', models.PositiveIntegerField(default=0, verbose_name='Сумма')),
                ('note', models.CharField(max_length=200, verbose_name='Примечание')),
            ],
        ),
    ]
