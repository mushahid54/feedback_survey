# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_survey', '0010_auto_20170510_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_survey.Student'),
        ),
    ]
