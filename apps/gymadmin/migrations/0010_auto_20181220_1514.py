# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0009_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='user_payments',
            new_name='user_payment',
        ),
    ]
