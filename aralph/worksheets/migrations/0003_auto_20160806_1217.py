# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-06 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksheets', '0002_auto_20160803_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.IntegerField(choices=[(1, 'Worksheet'), (2, 'Video Tutorial'), (3, 'Quiz')], default=1),
        ),
    ]
