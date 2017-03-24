# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20170324_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='joining_date',
            field=models.DateField(help_text=b'DD/MM/YYYY', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(help_text=b'DD/MM/YYYY', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.PositiveSmallIntegerField(choices=[(1, b'Male'), (2, b'Female')], null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='work_location',
            field=models.CharField(max_length=30),
        ),
    ]
