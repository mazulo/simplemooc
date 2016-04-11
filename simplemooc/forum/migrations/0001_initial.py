# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(related_name='replies', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['-correct', 'created'],
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('slug', models.SlugField(verbose_name='Identificador', unique=True, max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(blank=True, verbose_name='Visualizações', default=0)),
                ('answers', models.IntegerField(blank=True, verbose_name='Respostas', default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(related_name='threads', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
                'ordering': ['-modified'],
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(related_name='replies', verbose_name='Tópico', to='forum.Thread'),
        ),
    ]
