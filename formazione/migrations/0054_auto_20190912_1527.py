# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-09-12 15:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formazione', '0053_auto_20190912_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corsobase',
            name='max_participants',
            field=models.SmallIntegerField(default=30, verbose_name='Massimo partecipanti'),
        ),
        migrations.AlterField(
            model_name='corsobase',
            name='min_participants',
            field=models.SmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(10)], verbose_name='Minimo partecipanti'),
        ),
    ]
