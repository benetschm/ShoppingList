# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-03 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingListApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoopingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homelocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppingListApp.HomeLocation')),
                ('storelocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppingListApp.StoreLocation')),
            ],
        ),
    ]
