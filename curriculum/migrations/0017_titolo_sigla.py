# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-08-28 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0016_auto_20190805_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='titolo',
            name='sigla',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]