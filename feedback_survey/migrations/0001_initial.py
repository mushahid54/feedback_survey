# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 06:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_survey.Course')),
                ('feedback_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_survey.Feedback')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SectionField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('field_type', models.CharField(max_length=20)),
                ('nested_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_survey.SectionField')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='section_fields',
            field=models.ManyToManyField(to='feedback_survey.SectionField'),
        ),
        migrations.AddField(
            model_name='feedbacktemplate',
            name='sections',
            field=models.ManyToManyField(to='feedback_survey.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback_survey.Teacher'),
        ),
    ]
