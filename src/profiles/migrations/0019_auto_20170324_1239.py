# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-24 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20170324_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=b'profile/avatar'),
        ),
    ]
