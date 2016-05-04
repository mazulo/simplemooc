# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.core.validators
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, verbose_name='Nome de Usuário', max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, números e @/./+/-/_', 'invalid')])),
                ('email', models.EmailField(unique=True, verbose_name='E-mail', max_length=254)),
                ('name', models.CharField(verbose_name='Nome', blank=True, max_length=100)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('key', models.CharField(unique=True, verbose_name='Chave', max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
            ],
            options={
                'verbose_name': 'Nova senha',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Novas senhas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True, auto_created=True)),
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
            field=models.ForeignKey(related_name='resets', verbose_name='Usuário para recuperação de senha', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, to='auth.Permission'),
        ),
    ]
