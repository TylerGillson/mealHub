# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170309_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.IntegerField(default=0),
        ),
    ]