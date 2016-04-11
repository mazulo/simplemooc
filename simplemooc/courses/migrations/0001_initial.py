# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='título', max_length=100)),
                ('content', models.TextField(verbose_name='conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'anúncio',
                'verbose_name_plural': 'anúncios',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CategoryDimensionCognitiveProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('comment', models.TextField(verbose_name='comentário')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('announcement', models.ForeignKey(related_name='comments', verbose_name='anúncio', to='courses.Announcement')),
                ('user', models.ForeignKey(verbose_name='usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comentário',
                'verbose_name_plural': 'comentários',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(verbose_name='descrição curta', blank=True)),
                ('about', models.TextField(verbose_name='sobre o curso', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('start_date', models.DateField(null=True, verbose_name='data de início', blank=True)),
                ('image', models.ImageField(null=True, upload_to='courses/images', verbose_name='imagem', blank=True)),
            ],
            options={
                'verbose_name': 'curso',
                'verbose_name_plural': 'cursos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], verbose_name='situação', default=1, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name_plural': 'inscrições',
                'verbose_name': 'inscrição',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
                ('number', models.IntegerField(verbose_name='número (ordem)', default=0, blank=True)),
                ('release_date', models.DateField(null=True, verbose_name='data de liberação', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'aula',
                'verbose_name_plural': 'aulas',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('embedded', models.TextField(verbose_name='vídeo embedded', blank=True)),
                ('material_file', models.FileField(null=True, upload_to='lessons/material', blank=True)),
                ('lesson', models.ForeignKey(related_name='materiais', verbose_name='aula', to='courses.Lesson')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiais',
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='verbo', max_length=100)),
                ('educational_goal', models.TextField(null=True, verbose_name='objetivo educacional', blank=True)),
                ('category_dimension', models.ForeignKey(related_name='verbs', verbose_name='categoria da dimensão processo cognitivo', to='courses.CategoryDimensionCognitiveProcess')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTRB',
            fields=[
                ('course_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to='courses.Course')),
            ],
            options={
                'verbose_name': 'curso Taxonomia Revisada de Bloom',
                'verbose_name_plural': 'cursos Taxonomia Revisada de Bloom',
            },
            bases=('courses.course',),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(related_name='lessons', verbose_name='Curso', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='knowledgelevel',
            name='lessons',
            field=models.ManyToManyField(related_name='levels', verbose_name='lição', to='courses.Lesson'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(related_name='enrollments', verbose_name='curso', to='courses.Course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(related_name='enrollments', verbose_name='usuário', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(related_name='courses', verbose_name='professor', to='accounts.Professor'),
        ),
        migrations.AddField(
            model_name='categorydimensioncognitiveprocess',
            name='lessons',
            field=models.ManyToManyField(verbose_name='categoria da dimensão processo cognitivo', to='courses.Lesson'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(related_name='announcements', verbose_name='curso', to='courses.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
