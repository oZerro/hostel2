# Generated by Django 4.0.5 on 2022-08-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otchet', '0008_alter_payments_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Имя'),
        ),
    ]
