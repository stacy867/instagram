# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-19 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0005_auto_20191018_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
