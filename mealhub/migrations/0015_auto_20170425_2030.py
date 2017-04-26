# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-26 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealhub', '0014_meal_date_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='time_available',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date_available',
            field=models.DateField(blank=True, null=True),
        ),
    ]
