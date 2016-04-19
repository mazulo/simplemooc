# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialTRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('embedded', models.TextField(blank=True, verbose_name='vídeo embedded')),
                ('material_file', models.FileField(blank=True, upload_to='lessons/material', null=True)),
                ('lesson', models.ForeignKey(verbose_name='aula', related_name='materiais', to='courses.LessonTRB')),
            ],
            options={
                'verbose_name_plural': 'materiais',
                'verbose_name': 'material',
            },
        ),
    ]
