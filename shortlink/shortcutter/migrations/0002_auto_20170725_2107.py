# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortcutter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Links',
        ),
    ]
