# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='photo',
            field=models.ImageField(blank=True, upload_to='meals/%Y/%m/%d'),
        ),
    ]