# Generated by Django 4.0.5 on 2022-09-10 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0023_departures_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='otchet.room', verbose_name='Комната'),
        ),
    ]
