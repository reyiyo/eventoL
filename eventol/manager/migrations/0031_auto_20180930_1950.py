# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-30 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_attendee_customfields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customfield',
            unique_together=set([('form', 'slug')]),
        ),
    ]
