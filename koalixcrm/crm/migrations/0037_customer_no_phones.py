# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0036_auto_20180221_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='no_phones',
            field=models.IntegerField(blank=True, null=True, verbose_name='No Phones'),
        ),
    ]
