# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0045_remove_person_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPersonAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_association', to='crm.Contact')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_association', to='crm.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='customerpersonassociation',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customerpersonassociation',
            name='person',
        ),
        migrations.DeleteModel(
            name='CustomerPersonAssociation',
        ),
        migrations.AddField(
            model_name='contact',
            name='people',
            field=models.ManyToManyField(blank=True, through='crm.ContactPersonAssociation', to='crm.Person', verbose_name='Has contact'),
        ),
        migrations.AddField(
            model_name='person',
            name='companies',
            field=models.ManyToManyField(blank=True, through='crm.ContactPersonAssociation', to='crm.Contact', verbose_name='Works at'),
        ),
    ]