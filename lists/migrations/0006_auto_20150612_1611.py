# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20150612_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.TextField(verbose_name=lists.models.List, default=None),
        ),
    ]
