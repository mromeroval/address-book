# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-08 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20161208_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
