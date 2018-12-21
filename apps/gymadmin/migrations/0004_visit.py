# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-13 14:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gymadmin', '0003_user_card_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(default=datetime.datetime.now)),
                ('users_visit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='gymadmin.User')),
            ],
        ),
    ]
