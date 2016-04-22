# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings
import django.contrib.auth.models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='Nome de Usuário', validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, números e @/./+/-/_', 'invalid')], max_length=30, unique=True)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254, unique=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='Data de entrada', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('key', models.CharField(verbose_name='Chave', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'Nova senha',
                'verbose_name_plural': 'Novas senhas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, parent_link=True, auto_created=True, serialize=False)),
            ],
            options={
                'verbose_name': 'professor',
                'verbose_name_plural': 'professores',
            },
            bases=('accounts.user',),
        ),
        migrations.AddField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(verbose_name='Usuário para recuperação de senha', to=settings.AUTH_USER_MODEL, related_name='resets'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='auth.Group', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', blank=True),
        ),
    ]
