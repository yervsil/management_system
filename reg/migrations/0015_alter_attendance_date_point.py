# Generated by Django 4.1.1 on 2022-11-24 15:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0014_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 15, 58, 16, 50454, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField()),
                ('att', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reg.attendance')),
            ],
        ),
    ]
