# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_text', models.CharField(max_length=50)),
            ],
        ),
    ]
