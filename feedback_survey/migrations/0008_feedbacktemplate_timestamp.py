# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_survey', '0007_sectionfield_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacktemplate',
            name='timestamp',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
