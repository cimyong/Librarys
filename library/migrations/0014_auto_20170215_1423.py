# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20170215_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(default=b'', max_length=1024),
        ),
    ]
