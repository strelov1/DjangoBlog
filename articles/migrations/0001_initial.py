# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('update_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-create_at',),
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]