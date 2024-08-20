# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='auto_processing_node',
            field=models.BooleanField(default=True, help_text='A flag indicating whether this task should be automatically assigned a processing node'),
        ),
    ]
