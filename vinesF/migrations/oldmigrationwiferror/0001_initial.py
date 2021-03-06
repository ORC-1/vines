# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='latest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primaryName', models.CharField(max_length=100)),
                ('Origin', models.CharField(max_length=200)),
                ('PreferredAudience', models.CharField(max_length=40)),
                ('Date', models.DateField()),
                ('Link', models.URLField()),
                #('LPath', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='videoID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoIDs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='viewcounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumViews', models.IntegerField(default=0)),
                ('videoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinesF.videoID')),
            ],
        ),
        migrations.AddField(
            model_name='latest',
            name='Lview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinesF.videoID'),
        ),
    ]
