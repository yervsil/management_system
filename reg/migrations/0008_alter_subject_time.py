# Generated by Django 4.1.1 on 2022-11-13 15:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_remove_subject_end_time_remove_subject_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='time',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), default=list, size=None),
        ),
    ]
