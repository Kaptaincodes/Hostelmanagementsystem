# Generated by Django 2.2 on 2020-04-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0004_visitor_no_of_rooms_required'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='no_of_rooms_required',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='to_date',
        ),
        migrations.AlterField(
            model_name='visitor',
            name='room_number',
            field=models.CharField(choices=[('PJAH', 'PJAH'), ('JAH', 'JAH'), ('DLW', 'DLW'), ('UFH', 'UFH')], default='PJAH', max_length=5),
        ),
    ]
