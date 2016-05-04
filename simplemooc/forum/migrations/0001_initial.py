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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(related_name='replies', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resposta',
                'ordering': ['-correct', 'created'],
                'verbose_name_plural': 'Respostas',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(verbose_name='Visualizações', blank=True, default=0)),
                ('answers', models.IntegerField(verbose_name='Respostas', blank=True, default=0)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(related_name='threads', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ],
            options={
                'verbose_name': 'Tópico',
                'ordering': ['-modified'],
                'verbose_name_plural': 'Tópicos',
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(related_name='replies', verbose_name='Tópico', to='forum.Thread'),
        ),
    ]
