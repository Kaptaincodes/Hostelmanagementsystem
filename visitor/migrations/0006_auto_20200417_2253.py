# Generated by Django 2.2 on 2020-04-17 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0005_auto_20200417_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='hostel_name',
            field=models.CharField(choices=[('PJAH', 'PJAH'), ('JAH', 'JAH'), ('DLW', 'DLW'), ('UFH', 'UFH')], default='PJAH', max_length=5),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='room_number',
            field=models.CharField(max_length=5),
        ),
    ]
