# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_survey', '0014_auto_20170510_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
