# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingListApp', '0002_shoopingitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShoopingItem',
            new_name='ShoppingItem',
        ),
    ]
