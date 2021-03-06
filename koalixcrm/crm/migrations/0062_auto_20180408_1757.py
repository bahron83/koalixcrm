# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0061_product_attribute_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductForCustomer',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.Product')),
                ('service_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Service Type')),
                ('expire_date', models.DateTimeField(blank=True, null=True, verbose_name='Expire Date')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_association', to='crm.Customer')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_association', to='crm.Supplier')),
            ],
            options={
                'verbose_name': 'Phone System',
                'verbose_name_plural': 'Phone System',
            },
            bases=('crm.product',),
        ),
        migrations.RemoveField(
            model_name='phonesystemforcustomer',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='phonesystemforcustomer',
            name='phonesystem_ptr',
        ),
        migrations.RemoveField(
            model_name='phonesystemforcustomer',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='PhoneSystem',
        ),
        migrations.DeleteModel(
            name='PhoneSystemForCustomer',
        ),
    ]
