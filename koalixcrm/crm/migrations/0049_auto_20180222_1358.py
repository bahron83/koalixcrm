# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0048_auto_20180222_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='addressline3',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='addressline4',
        ),
    ]
