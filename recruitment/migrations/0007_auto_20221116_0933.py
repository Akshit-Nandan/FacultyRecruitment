# Generated by Django 2.2.24 on 2022-11-16 04:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0006_auto_20220925_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 16, 4, 3, 12, 702016, tzinfo=utc)),
        ),
    ]