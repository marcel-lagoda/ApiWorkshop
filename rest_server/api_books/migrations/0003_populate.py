# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from api_books.worker import populate_db


def populate(apps, schema_editor):
    populate_db()


class Migration(migrations.Migration):

    dependencies = [
        ('api_books', '0002_auto_20161201_1705'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
