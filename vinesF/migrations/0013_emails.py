# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-15 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinesF', '0012_auto_20180606_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]