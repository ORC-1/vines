# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-05 02:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vinesF', '0008_auto_20180523_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitbck2bck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinesF.video')),
            ],
        ),
        migrations.RemoveField(
            model_name='latest',
            name='Added',
        ),
        migrations.RemoveField(
            model_name='latest',
            name='Lview',
        ),
        migrations.DeleteModel(
            name='latest',
        ),
    ]
