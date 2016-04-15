# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160406_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorydimensioncognitiveprocess',
            options={'verbose_name_plural': 'categorias da dimensão processo cognitivo', 'verbose_name': 'categoria da dimensão processo cognitivo'},
        ),
        migrations.AlterModelOptions(
            name='knowledgelevel',
            options={'verbose_name_plural': 'níveis de conhecimento', 'verbose_name': 'nível de conhecimento'},
        ),
        migrations.AlterModelOptions(
            name='verb',
            options={'verbose_name_plural': 'verbos', 'verbose_name': 'verbo'},
        ),
        migrations.RemoveField(
            model_name='categorydimensioncognitiveprocess',
            name='lessons',
        ),
        migrations.RemoveField(
            model_name='knowledgelevel',
            name='lessons',
        ),
        migrations.AddField(
            model_name='lessontrb',
            name='category_dimension',
            field=models.ManyToManyField(related_name='lessons', verbose_name='categoria processo cognitivo', to='courses.CategoryDimensionCognitiveProcess'),
        ),
        migrations.AddField(
            model_name='lessontrb',
            name='levels',
            field=models.ManyToManyField(related_name='lessons', verbose_name='levels', to='courses.KnowledgeLevel'),
        ),
    ]
