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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(default=False, verbose_name='Correta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Respostas',
                'ordering': ['-correct', 'created'],
                'verbose_name': 'Resposta',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Identificador')),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(blank=True, default=0, verbose_name='Visualizações')),
                ('answers', models.IntegerField(blank=True, default=0, verbose_name='Respostas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='threads', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Tópicos',
                'ordering': ['-modified'],
                'verbose_name': 'Tópico',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(verbose_name='Tópico', related_name='replies', to='forum.Thread'),
        ),
    ]
