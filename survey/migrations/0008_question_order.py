# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-10-24 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_question_question_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
