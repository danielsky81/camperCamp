# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-06 20:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('new', 'new'), ('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done'), ('rejected', 'rejected'), ('require data', 'require data')], default='new', max_length=12)),
                ('item_type', models.CharField(choices=[('issue', 'issue'), ('feature', 'feature')], max_length=7)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_date', models.DateTimeField(auto_now_add=True)),
                ('votes_number', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_votes', to=settings.AUTH_USER_MODEL)),
                ('voted_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='items.Items')),
            ],
        ),
        migrations.AddField(
            model_name='itemcomments',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_comments', to='items.Items'),
        ),
    ]
