# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0072_auto_20180510_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneSystemForCustomer',
            fields=[
                ('productforcustomer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.ProductForCustomer')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year of installation')),
                ('no_ext_lines', models.IntegerField(blank=True, null=True, verbose_name='External lines')),
                ('no_int_lines', models.IntegerField(blank=True, null=True, verbose_name='Internal lines')),
            ],
            options={
                'verbose_name': 'Phone System',
                'verbose_name_plural': 'Phone Systems',
            },
            bases=('crm.productforcustomer',),
        ),
    ]
