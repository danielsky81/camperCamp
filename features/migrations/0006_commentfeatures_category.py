# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-27 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_auto_20190726_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentfeatures',
            name='category',
            field=models.CharField(choices=[('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')], default='to do', max_length=12),
        ),
    ]
