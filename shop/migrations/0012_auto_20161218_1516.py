# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-18 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20161218_1445'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('product', 'weight')]),
        ),
    ]
