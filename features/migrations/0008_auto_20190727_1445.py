# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-27 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_commentfeatures_user_votes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='votes',
            new_name='user_votes',
        ),
        migrations.RemoveField(
            model_name='commentfeatures',
            name='category',
        ),
        migrations.RemoveField(
            model_name='commentfeatures',
            name='user_votes',
        ),
        migrations.AddField(
            model_name='feature',
            name='category',
            field=models.CharField(choices=[('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')], default='to do', max_length=12),
        ),
    ]
