# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_meal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]