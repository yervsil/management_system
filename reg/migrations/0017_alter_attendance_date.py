# Generated by Django 4.1.1 on 2022-12-11 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0016_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 11, 15, 11, 861459, tzinfo=datetime.timezone.utc)),
        ),
    ]
