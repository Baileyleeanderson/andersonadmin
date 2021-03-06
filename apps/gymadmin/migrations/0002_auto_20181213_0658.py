# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-13 06:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='signup_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='contract_expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_paid',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
