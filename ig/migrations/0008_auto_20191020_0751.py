# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ig', '0007_auto_20191020_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
