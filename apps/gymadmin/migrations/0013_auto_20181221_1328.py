# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0012_cafe_expense_walkin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='payment_date',
            field=models.DateTimeField(default=''),
        ),
    ]
