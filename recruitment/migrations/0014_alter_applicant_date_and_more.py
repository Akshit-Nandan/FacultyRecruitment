# Generated by Django 4.2 on 2023-04-09 05:52

import datetime
from django.db import migrations, models
import recruitment.models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0013_merge_20230409_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 4, 9, 5, 52, 43, 612291, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='general',
            name='reservation_certificate',
            field=models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded),
        ),
    ]