# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-07 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealhub', '0006_auto_20170407_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_available',
            field=models.DateField(),
        ),
    ]
