# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-01 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20171101_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.ManyToManyField(to='notes.Tag'),
        ),
    ]
