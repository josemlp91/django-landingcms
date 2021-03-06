# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paginahome',
            name='boton1_enlace',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boton1enlace', to='content.LinkContent'),
        ),
        migrations.AddField(
            model_name='paginahome',
            name='boton1_texto',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boton1texto', to='content.TitleContent'),
        ),
        migrations.AddField(
            model_name='paginahome',
            name='texto1_banner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texto1banner', to='content.TitleContent'),
        ),
    ]
