# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-18 17:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0004_auto_20191018_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]
