# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-26 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_auto_20190726_1020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentFeatures',
        ),
    ]