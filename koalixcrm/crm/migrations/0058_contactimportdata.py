# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0057_visitforcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(max_length=255, upload_to='data_files')),
                ('contact_type', models.CharField(choices=[('C', 'Customer'), ('S', 'Supplier')], max_length=1, verbose_name='Contact Type')),
            ],
            options={
                'verbose_name': 'Contact: Import Data from XLSX file',
                'verbose_name_plural': 'Contacts: Import Data from XLSX file',
            },
        ),
    ]