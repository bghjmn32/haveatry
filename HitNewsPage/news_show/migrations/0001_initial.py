# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-02 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('title', models.TextField()),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]
