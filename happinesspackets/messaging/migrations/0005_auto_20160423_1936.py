# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_auto_20160403_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='message',
            name='admin_approved_public',
            field=models.BooleanField(default=False),
        ),
    ]
