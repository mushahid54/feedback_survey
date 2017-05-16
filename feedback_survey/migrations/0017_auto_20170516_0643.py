# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_survey', '0016_remove_feedback_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sectionfield',
            old_name='nested_section',
            new_name='parent_section',
        ),
        migrations.AddField(
            model_name='feedbacktemplate',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]