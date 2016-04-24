# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='título')),
                ('content', models.TextField(verbose_name='conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name_plural': 'anúncios',
                'ordering': ['-created_at'],
                'verbose_name': 'anúncio',
            },
        ),
        migrations.CreateModel(
            name='CategoryCognitiveProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name_plural': 'categorias da dimensão processo cognitivo',
                'verbose_name': 'categoria da dimensão processo cognitivo',
            },
        ),
        migrations.CreateModel(
            name='ChooseCategoryCognitiveProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name_plural': 'escolhas das categorias da dimensão        processo cognitivo',
                'verbose_name': 'escolha da categoria da dimensão processo cognitivo',
            },
        ),
        migrations.CreateModel(
            name='ChooseKnowledgeLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name_plural': 'escolhas níveis de conhecimento',
                'verbose_name': 'escolha nível de conhecimento',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('comment', models.TextField(verbose_name='comentário')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('announcement', models.ForeignKey(verbose_name='anúncio', related_name='comments', to='courses.Announcement')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name_plural': 'comentários',
                'ordering': ['created_at'],
                'verbose_name': 'comentário',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(blank=True, verbose_name='descrição curta')),
                ('about', models.TextField(blank=True, verbose_name='sobre o curso')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='data de início')),
                ('image', models.ImageField(blank=True, upload_to='courses/images', null=True, verbose_name='imagem')),
                ('professor', models.ForeignKey(verbose_name='professor', related_name='courses_course_courses', to='accounts.Professor')),
            ],
            options={
                'verbose_name_plural': 'cursos',
                'ordering': ['name'],
                'verbose_name': 'curso',
            },
        ),
        migrations.CreateModel(
            name='CourseRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='nome do curso')),
                ('description', models.TextField(blank=True, verbose_name='descrição curta')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de início do curso')),
                ('is_trb', models.BooleanField(default=False, verbose_name='Curso usará ferramentas pedagógicas de apoio?')),
                ('date_requested', models.DateTimeField(auto_now_add=True, verbose_name='Data da requisição')),
                ('professor', models.ForeignKey(verbose_name='professor', related_name='course_requests', to='accounts.Professor')),
            ],
            options={
                'verbose_name_plural': 'requisições de cursos',
                'verbose_name': 'requisição de curso',
            },
        ),
        migrations.CreateModel(
            name='CourseTRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('slug', models.SlugField(verbose_name='atalho')),
                ('description', models.TextField(blank=True, verbose_name='descrição curta')),
                ('about', models.TextField(blank=True, verbose_name='sobre o curso')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='data de início')),
                ('image', models.ImageField(blank=True, upload_to='courses/images', null=True, verbose_name='imagem')),
                ('professor', models.ForeignKey(verbose_name='professor', related_name='courses_coursetrb_courses', to='accounts.Professor')),
            ],
            options={
                'verbose_name_plural': 'cursos Taxonomia Revisada de Bloom',
                'verbose_name': 'curso Taxonomia Revisada de Bloom',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=1, verbose_name='situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(verbose_name='usuário', related_name='enrollments', to=settings.AUTH_USER_MODEL)),
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
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
            ],
            options={
                'verbose_name_plural': 'níveis de conhecimento',
                'verbose_name': 'nível de conhecimento',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='número (ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('course', models.ForeignKey(verbose_name='Curso', related_name='lessons', to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'aulas',
                'ordering': ['number'],
                'verbose_name': 'aula',
            },
        ),
        migrations.CreateModel(
            name='LessonTRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='número (ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('uptade_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('course', models.ForeignKey(verbose_name='curso utilizando Ferramenta Pedagógica de Apoio', related_name='lessonstrb', to='courses.CourseTRB')),
            ],
            options={
                'verbose_name_plural': 'aulas curso taxonomia revisada de bloom',
                'verbose_name': 'aula curso taxonomia revisada de bloom',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('embedded', models.TextField(blank=True, verbose_name='vídeo embedded')),
                ('material_file', models.FileField(blank=True, upload_to='lessons/material', null=True)),
                ('lesson', models.ForeignKey(verbose_name='aula', related_name='materiais', to='courses.Lesson')),
            ],
            options={
                'verbose_name_plural': 'materiais',
                'verbose_name': 'material',
            },
        ),
        migrations.CreateModel(
            name='MaterialTRB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('embedded', models.TextField(blank=True, verbose_name='vídeo embedded')),
                ('material_file', models.FileField(blank=True, upload_to='lessons/material', null=True)),
                ('lesson', models.ForeignKey(verbose_name='aula', related_name='materiais', to='courses.LessonTRB')),
            ],
            options={
                'verbose_name_plural': 'materiais',
                'verbose_name': 'material',
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='verbo')),
                ('educational_goal', models.TextField(blank=True, null=True, verbose_name='objetivo educacional')),
                ('category_dimension', models.ForeignKey(verbose_name='categoria da dimensão processo cognitivo', related_name='verbs', to='courses.CategoryCognitiveProcess')),
            ],
            options={
                'verbose_name_plural': 'verbos',
                'verbose_name': 'verbo',
            },
        ),
        migrations.AddField(
            model_name='knowledgelevel',
            name='lesson',
            field=models.ForeignKey(verbose_name='lição', related_name='levels', to='courses.LessonTRB'),
        ),
        migrations.AddField(
            model_name='categorycognitiveprocess',
            name='lesson',
            field=models.ForeignKey(verbose_name='lição', related_name='categories_dimension', to='courses.LessonTRB'),
        ),
        migrations.AddField(
            model_name='categorycognitiveprocess',
            name='level',
            field=models.ForeignKey(verbose_name='nível de conhecimento', related_name='categories_dimension', to='courses.KnowledgeLevel'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(verbose_name='curso', related_name='announcements', to='courses.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
    ]
