# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingListApp', '0003_auto_20161103_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingitem',
            name='homelocation',
        ),
        migrations.RemoveField(
            model_name='shoppingitem',
            name='storelocation',
        ),
        migrations.DeleteModel(
            name='ShoppingItem',
        ),
    ]
