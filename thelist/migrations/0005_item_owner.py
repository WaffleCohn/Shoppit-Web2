# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-17 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thelist', '0004_auto_20160417_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='thelist.Profile'),
            preserve_default=False,
        ),
    ]