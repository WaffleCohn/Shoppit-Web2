# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thelist', '0006_item_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]