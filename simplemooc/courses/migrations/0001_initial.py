# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(verbose_name='título', max_length=100)),
                ('content', models.TextField(verbose_name='conteúdo')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'anúncio',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'anúncios',
            },
        ),
        migrations.CreateModel(
            name='CategoryCognitiveProcess',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
            options={
                'verbose_name': 'categoria da dimensão processo cognitivo',
                'verbose_name_plural': 'categorias da dimensão processo cognitivo',
            },
        ),
        migrations.CreateModel(
            name='ChooseCategoryCognitiveProcess',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
            options={
                'verbose_name': 'escolha da categoria da dimensão processo cognitivo',
                'verbose_name_plural': 'escolhas das categorias da dimensão        processo cognitivo',
            },
        ),
        migrations.CreateModel(
            name='ChooseKnowledgeLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
            options={
                'verbose_name': 'escolha nível de conhecimento',
                'verbose_name_plural': 'escolhas níveis de conhecimento',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('comment', models.TextField(verbose_name='comentário')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('announcement', models.ForeignKey(related_name='comments', verbose_name='anúncio', to='courses.Announcement')),
                ('user', models.ForeignKey(verbose_name='usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comentário',
                'ordering': ['created_at'],
                'verbose_name_plural': 'comentários',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(verbose_name='descrição curta', blank=True)),
                ('about', models.TextField(verbose_name='sobre o curso', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('start_date', models.DateField(verbose_name='data de início', blank=True, null=True)),
                ('image', models.ImageField(verbose_name='imagem', blank=True, null=True, upload_to='courses/images')),
                ('professor', models.ForeignKey(related_name='courses_course_courses', verbose_name='professor', to='accounts.Professor')),
            ],
            options={
                'verbose_name': 'curso',
                'ordering': ['name'],
                'verbose_name_plural': 'cursos',
            },
        ),
        migrations.CreateModel(
            name='CourseRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome do curso', max_length=150)),
                ('description', models.TextField(verbose_name='descrição curta', blank=True)),
                ('start_date', models.DateField(verbose_name='Data de início do curso', blank=True, null=True)),
                ('is_trb', models.BooleanField(verbose_name='Curso usará ferramentas pedagógicas de apoio?', default=False)),
                ('date_requested', models.DateTimeField(verbose_name='Data da requisição', auto_now_add=True)),
                ('professor', models.ForeignKey(related_name='course_requests', verbose_name='professor', to='accounts.Professor')),
            ],
            options={
                'verbose_name': 'requisição de curso',
                'verbose_name_plural': 'requisições de cursos',
            },
        ),
        migrations.CreateModel(
            name='CourseTRB',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(verbose_name='descrição curta', blank=True)),
                ('about', models.TextField(verbose_name='sobre o curso', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('start_date', models.DateField(verbose_name='data de início', blank=True, null=True)),
                ('image', models.ImageField(verbose_name='imagem', blank=True, null=True, upload_to='courses/images')),
                ('professor', models.ForeignKey(related_name='courses_coursetrb_courses', verbose_name='professor', to='accounts.Professor')),
            ],
            options={
                'verbose_name': 'curso Taxonomia Revisada de Bloom',
                'verbose_name_plural': 'cursos Taxonomia Revisada de Bloom',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], blank=True, default=1, verbose_name='situação')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(related_name='enrollments', verbose_name='usuário', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeLevel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
            ],
            options={
                'verbose_name': 'nível de conhecimento',
                'verbose_name_plural': 'níveis de conhecimento',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
                ('number', models.IntegerField(verbose_name='número (ordem)', blank=True, default=0)),
                ('release_date', models.DateField(verbose_name='data de liberação', blank=True, null=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('course', models.ForeignKey(related_name='lessons', verbose_name='Curso', to='courses.Course')),
            ],
            options={
                'verbose_name': 'aula',
                'ordering': ['number'],
                'verbose_name_plural': 'aulas',
            },
        ),
        migrations.CreateModel(
            name='LessonTRB',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('description', models.TextField(verbose_name='descrição', blank=True)),
                ('number', models.IntegerField(verbose_name='número (ordem)', blank=True, default=0)),
                ('release_date', models.DateField(verbose_name='data de liberação', blank=True, null=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('uptade_at', models.DateTimeField(verbose_name='atualizado em', auto_now=True)),
                ('course', models.ForeignKey(related_name='lessonstrb', verbose_name='curso utilizando Ferramenta Pedagógica de Apoio', to='courses.CourseTRB')),
            ],
            options={
                'verbose_name': 'aula curso taxonomia revisada de bloom',
                'verbose_name_plural': 'aulas curso taxonomia revisada de bloom',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('embedded', models.TextField(verbose_name='vídeo embedded', blank=True)),
                ('material_file', models.FileField(blank=True, null=True, upload_to='lessons/material')),
                ('lesson', models.ForeignKey(related_name='materiais', verbose_name='aula', to='courses.Lesson')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiais',
            },
        ),
        migrations.CreateModel(
            name='MaterialTRB',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='nome', max_length=100)),
                ('embedded', models.TextField(verbose_name='vídeo embedded', blank=True)),
                ('material_file', models.FileField(blank=True, null=True, upload_to='lessons/material')),
                ('lesson', models.ForeignKey(related_name='materiais', verbose_name='aula', to='courses.LessonTRB')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiais',
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='verbo', max_length=100)),
                ('educational_goal', models.TextField(verbose_name='objetivo educacional', blank=True, null=True)),
                ('category_dimension', models.ForeignKey(related_name='verbs', verbose_name='categoria da dimensão processo cognitivo', to='courses.CategoryCognitiveProcess')),
            ],
            options={
                'verbose_name': 'verbo',
                'verbose_name_plural': 'verbos',
            },
        ),
        migrations.AddField(
            model_name='knowledgelevel',
            name='lesson',
            field=models.ForeignKey(related_name='levels', verbose_name='lição', to='courses.LessonTRB'),
        ),
        migrations.AddField(
            model_name='categorycognitiveprocess',
            name='lesson',
            field=models.ForeignKey(related_name='categories_dimension', verbose_name='lição', to='courses.LessonTRB'),
        ),
        migrations.AddField(
            model_name='categorycognitiveprocess',
            name='level',
            field=models.ForeignKey(related_name='categories_dimension', verbose_name='nível de conhecimento', to='courses.KnowledgeLevel'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
    ]
