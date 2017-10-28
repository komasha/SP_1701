# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='smileage',
            new_name='available_smileage',
        ),
        migrations.AddField(
            model_name='user',
            name='used_smileage',
            field=models.IntegerField(default=0),
        ),
    ]
