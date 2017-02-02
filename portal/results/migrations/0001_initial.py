# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('surname', models.CharField(blank=True, max_length=21, null=True)),
                ('othernames', models.CharField(blank=True, max_length=22, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('nationality', models.CharField(blank=True, max_length=14, null=True)),
                ('program', models.CharField(blank=True, max_length=69, null=True)),
                ('regnumber', models.CharField(blank=True, max_length=18, null=True)),
                ('entrymode', models.CharField(blank=True, max_length=14, null=True)),
                ('doe', models.CharField(blank=True, max_length=18, null=True)),
                ('dob', models.CharField(blank=True, max_length=19, null=True)),
                ('academicyear', models.CharField(blank=True, max_length=9, null=True)),
                ('examperiod', models.CharField(blank=True, max_length=14, null=True)),
                ('coursecode', models.CharField(blank=True, max_length=49, null=True)),
                ('coursename', models.CharField(blank=True, max_length=89, null=True)),
                ('coursework', models.CharField(blank=True, max_length=4, null=True)),
                ('exam', models.CharField(blank=True, max_length=4, null=True)),
                ('programcode', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(blank=True, max_length=35, null=True)),
            ],
            options={
                'db_table': 'results',
                'managed': False,
            },
        ),
    ]
