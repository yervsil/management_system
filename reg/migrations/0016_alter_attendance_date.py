# Generated by Django 4.1.1 on 2022-12-04 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0015_alter_attendance_date_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 4, 13, 5, 21, 951757, tzinfo=datetime.timezone.utc)),
        ),
    ]
