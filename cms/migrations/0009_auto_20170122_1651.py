# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_paginahome_main_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paginahome',
            old_name='main_image',
            new_name='main_imagen',
        ),
    ]
