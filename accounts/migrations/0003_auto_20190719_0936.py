# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190719_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/default_profile_img.jpg', upload_to='img'),
        ),
    ]
