# Generated by Django 4.0.5 on 2022-09-10 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0021_alter_departures_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departures',
            name='user',
        ),
        migrations.AddField(
            model_name='departures',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='departures',
            name='phone_number',
            field=models.CharField(default='79876543412', max_length=11, verbose_name='Номер телефона'),
        ),
    ]