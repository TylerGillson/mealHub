# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-06 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mealhub', '0002_auto_20170405_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='meal_rating',
            new_name='review_rating',
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_rating',
            field=models.IntegerField(choices=[(0, 'No Stars'), (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')], default=0),
        ),
    ]
