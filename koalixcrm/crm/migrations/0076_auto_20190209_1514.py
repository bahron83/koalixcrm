# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-09 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0075_auto_20180519_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analogphoneforcustomer',
            options={'verbose_name': 'Telefono analogico', 'verbose_name_plural': 'Telefoni analogici'},
        ),
        migrations.AlterModelOptions(
            name='callforcontact',
            options={'verbose_name': 'Chiamata', 'verbose_name_plural': 'Chiamate'},
        ),
        migrations.AlterModelOptions(
            name='contactpersonassociation',
            options={'verbose_name': 'Contatti', 'verbose_name_plural': 'Contatti'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Clienti'},
        ),
        migrations.AlterModelOptions(
            name='digitalphoneforcustomer',
            options={'verbose_name': 'Telefono digitale', 'verbose_name_plural': 'Telefoni digitali'},
        ),
        migrations.AlterModelOptions(
            name='internetforcustomer',
            options={'verbose_name': 'Connessione Internet', 'verbose_name_plural': 'Connessioni Internet'},
        ),
        migrations.AlterModelOptions(
            name='mobileforcustomer',
            options={'verbose_name': 'Servizio mobile', 'verbose_name_plural': 'Servizi mobili'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Prodotto', 'verbose_name_plural': 'Prodotti'},
        ),
        migrations.AlterModelOptions(
            name='productforcustomer',
            options={'verbose_name': 'Prodotto', 'verbose_name_plural': 'Prodotti'},
        ),
        migrations.AlterModelOptions(
            name='switchboardforcustomer',
            options={'verbose_name': 'Centralino', 'verbose_name_plural': 'Centralini'},
        ),
        migrations.AlterModelOptions(
            name='visitforcontact',
            options={'verbose_name': 'Visita', 'verbose_name_plural': 'Visite'},
        ),
        migrations.AlterField(
            model_name='attribute',
            name='model_type',
            field=models.CharField(choices=[('V', 'Varchar'), ('I', 'Intero'), ('D', 'Decimal'), ('T', 'Testo')], max_length=1, verbose_name='Model Type'),
        ),
        migrations.AlterField(
            model_name='call',
            name='status',
            field=models.CharField(choices=[('P', 'Planned'), ('D', 'Delayed'), ('R', 'ToRecall'), ('F', 'Fallito'), ('S', 'Success')], default='P', max_length=1, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='callforcontact',
            name='cperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Person', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='customerbillingcycle',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='customergrouptransform',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='Prodotto'),
        ),
        migrations.AlterField(
            model_name='person',
            name='companies',
            field=models.ManyToManyField(blank=True, through='crm.ContactPersonAssociation', to='crm.Contact', verbose_name='Lavora per'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='position',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='Prodotto'),
        ),
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Quantità'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='town',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Città'),
        ),
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='Prodotto'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.Customer'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data scadenza'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='maintainer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Manutentore'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='Prodotto correlato'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantità'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='service_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo di servizio'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='crm.Supplier'),
        ),
        migrations.AlterField(
            model_name='productforcustomer',
            name='year',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Anno di installazione'),
        ),
        migrations.AlterField(
            model_name='switchboardforcustomer',
            name='external_lines',
            field=models.IntegerField(blank=True, null=True, verbose_name='Linee esterne'),
        ),
        migrations.AlterField(
            model_name='switchboardforcustomer',
            name='internal_lines',
            field=models.IntegerField(blank=True, null=True, verbose_name='Linee interne'),
        ),
        migrations.AlterField(
            model_name='textparagraphindocumenttemplate',
            name='text_paragraph',
            field=models.TextField(verbose_name='Testo'),
        ),
        migrations.AlterField(
            model_name='textparagraphinsalesdocument',
            name='text_paragraph',
            field=models.TextField(verbose_name='Testo'),
        ),
        migrations.AlterField(
            model_name='unittransform',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Product', verbose_name='Prodotto'),
        ),
        migrations.AlterField(
            model_name='visitforcontact',
            name='cperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Person', verbose_name='Persona'),
        ),
        migrations.AlterField(
            model_name='visitforcontact',
            name='ref_call',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.CallForContact', verbose_name='Rif. chiamata'),
        ),
    ]
