# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-10-17 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_titolopersonale_automatica'),
    ]

    operations = [
        migrations.AddField(
            model_name='titolo',
            name='area',
            field=models.CharField(blank=True, choices=[('1', 'Salute'), ('2', 'Sociale'), ('3', 'Emergenze'), ('4', 'Principi e valori'), ('5', 'Giovani'), ('6', 'Sviluppo')], db_index=True, max_length=1, null=True),
        ),
    ]
