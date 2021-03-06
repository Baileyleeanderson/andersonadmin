# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0011_payments_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default='', max_length=50)),
                ('item_purchased', models.CharField(default='', max_length=125)),
                ('amount', models.IntegerField(default=0, max_length=6)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_paid_for', models.CharField(default='', max_length=125)),
                ('note', models.CharField(default='', max_length=255)),
                ('amount', models.IntegerField(default=0, max_length=6)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Walkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(default='', max_length=50)),
                ('membership_purchased', models.CharField(default='', max_length=125)),
                ('amount', models.IntegerField(default=0, max_length=6)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
