# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='replies', verbose_name='Autor')),
            ],
            options={
                'ordering': ['-correct', 'created'],
                'verbose_name_plural': 'Respostas',
                'verbose_name': 'Resposta',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(verbose_name='Visualizações', default=0, blank=True)),
                ('answers', models.IntegerField(verbose_name='Respostas', default=0, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='threads', verbose_name='Autor')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem')),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name_plural': 'Tópicos',
                'verbose_name': 'Tópico',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(to='forum.Thread', related_name='replies', verbose_name='Tópico'),
        ),
    ]
