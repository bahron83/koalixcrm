# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 15:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0049_auto_20180222_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callforcontact',
            options={'verbose_name': 'Calls', 'verbose_name_plural': 'Calls'},
        ),
        migrations.AlterModelOptions(
            name='contactpersonassociation',
            options={'verbose_name': 'Contacts', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='phonesystemforcustomer',
            options={'verbose_name': 'Phone System', 'verbose_name_plural': 'Phone System'},
        ),
    ]
