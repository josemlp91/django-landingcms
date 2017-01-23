# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_remove_imagecontent_form'),
        ('cms', '0007_auto_20170122_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginahome',
            name='main_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mainimage', to='content.ImageContent'),
        ),
    ]
