# Generated by Django 2.2 on 2020-05-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_auto_20200519_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='is_departed',
            field=models.BooleanField(default=False, verbose_name='Cancelled'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Confirm Booking'),
        ),
    ]
