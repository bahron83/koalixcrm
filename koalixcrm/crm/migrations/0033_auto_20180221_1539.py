# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 15:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0032_customer_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallForContact',
            fields=[
                ('call_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='crm.Call')),
                ('purpose', models.CharField(choices=[('F', 'First commercial call'), ('S', 'Planned commercial call'), ('A', 'Assistance call')], max_length=1, verbose_name='Purpose')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Contact')),
            ],
            options={
                'verbose_name': 'Call For Contact',
                'verbose_name_plural': 'Call For Contact',
            },
            bases=('crm.call',),
        ),
        migrations.RenameField(
            model_name='call',
            old_name='default_customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='call',
            old_name='default_supplier',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='call',
            old_name='default_template_set',
            new_name='template_set',
        ),
        migrations.AddField(
            model_name='call',
            name='date_due',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date due'),
        ),
        migrations.AddField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('P', 'Planned'), ('D', 'Delayed'), ('R', 'ToRecall'), ('A', 'Failed')], default='P', max_length=1, verbose_name='Status'),
        ),
    ]
