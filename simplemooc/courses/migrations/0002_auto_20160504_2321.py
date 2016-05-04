# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(verbose_name='informar conteúdo', max_length=100),
        ),
        migrations.AlterField(
            model_name='lessontrb',
            name='name',
            field=models.CharField(verbose_name='informar conteúdo', max_length=100),
        ),
    ]
