# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170624_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, max_length=600, verbose_name='sumário'),
        ),
    ]
