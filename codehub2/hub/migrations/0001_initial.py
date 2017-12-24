# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-24 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('repo_path', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='project_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_commit',
            fields=[
                ('commit_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('commit_time', models.DateTimeField()),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.User')),
            ],
        ),
        migrations.AddField(
            model_name='project_user',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='lead_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.User'),
        ),
    ]
