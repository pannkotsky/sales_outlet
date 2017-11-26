# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 15:24
from __future__ import unicode_literals

import common.models
import common.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(4), common.validators.DigitValidator], verbose_name='Postal code')),
                ('city_name', models.CharField(max_length=15, verbose_name='City name')),
                ('street_name', models.CharField(max_length=20, verbose_name='Street name')),
                ('street_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)], verbose_name='Street number')),
                ('additional', models.CharField(blank=True, max_length=100, null=True, verbose_name='Additional info')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(5), common.validators.DigitValidator], verbose_name='Account number')),
                ('bank_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(4), common.validators.DigitValidator], verbose_name='Bank code')),
                ('bank_name', models.CharField(max_length=50, verbose_name='Bank name')),
            ],
            options={
                'verbose_name': 'Bank account',
                'verbose_name_plural': 'Bank accounts',
            },
        ),
        migrations.CreateModel(
            name='StreetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=5, unique=True, verbose_name='Short name')),
                ('short_name_en', models.CharField(max_length=5, null=True, unique=True, verbose_name='Short name')),
                ('short_name_uk', models.CharField(max_length=5, null=True, unique=True, verbose_name='Short name')),
                ('full_name', models.CharField(max_length=10, unique=True, verbose_name='Full name')),
                ('full_name_en', models.CharField(max_length=10, null=True, unique=True, verbose_name='Full name')),
                ('full_name_uk', models.CharField(max_length=10, null=True, unique=True, verbose_name='Full name')),
            ],
            options={
                'verbose_name': 'Street type',
                'verbose_name_plural': 'Street types',
            },
        ),
        migrations.AlterUniqueTogether(
            name='bankaccount',
            unique_together=set([('number', 'bank_code')]),
        ),
        migrations.AddField(
            model_name='address',
            name='street_type',
            field=models.ForeignKey(default=common.models.get_default_street_type, on_delete=django.db.models.deletion.PROTECT, to='common.StreetType', verbose_name='Street type'),
        ),
    ]
