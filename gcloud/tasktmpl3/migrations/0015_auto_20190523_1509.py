# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-23 07:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasktmpl3', '0014_remove_tasktemplate_business'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasktemplate',
            options={'ordering': ['-id'], 'verbose_name': '\u6d41\u7a0b\u6a21\u677f TaskTemplate', 'verbose_name_plural': '\u6d41\u7a0b\u6a21\u677f TaskTemplate'},
        ),
    ]