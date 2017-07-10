# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0003_screen_port'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='screen',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='screengroup',
            name='screens',
        ),
        migrations.AddField(
            model_name='screen',
            name='groups',
            field=models.ManyToManyField(to='screens.ScreenGroup'),
        ),
    ]
