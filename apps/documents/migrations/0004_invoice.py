# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20171129_2118'),
        ('documents', '0003_auto_20171129_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('number', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Number')),
                ('date', models.DateField(verbose_name='Date')),
                ('product_quantity', models.IntegerField(verbose_name='Product quantity')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='documents.Contract', verbose_name='Contract')),
                ('packaging', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='products.Packaging', verbose_name='Packaging')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='products.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]