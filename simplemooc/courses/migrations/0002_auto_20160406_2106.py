# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTRB',
            fields=[
                ('lesson_ptr', models.OneToOneField(to='courses.Lesson', primary_key=True, parent_link=True, serialize=False, auto_created=True)),
            ],
            options={
                'verbose_name': 'aula curso taxonomia revisada de bloom',
                'verbose_name_plural': 'aulas curso taxonomia revisada de bloom',
            },
            bases=('courses.lesson',),
        ),
        migrations.AlterField(
            model_name='categorydimensioncognitiveprocess',
            name='lessons',
            field=models.ManyToManyField(verbose_name='categoria da dimensão processo cognitivo', related_name='categoriesdcp', to='courses.LessonTRB'),
        ),
        migrations.AlterField(
            model_name='knowledgelevel',
            name='lessons',
            field=models.ManyToManyField(verbose_name='lição', related_name='levels', to='courses.LessonTRB'),
        ),
    ]
