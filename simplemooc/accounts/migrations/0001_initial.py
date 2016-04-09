# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import re
import django.contrib.auth.models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, números e @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário', max_length=30, unique=True)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=254, unique=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de entrada')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('key', models.CharField(verbose_name='Chave', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('confirmed', models.BooleanField(verbose_name='Confirmado?', default=False)),
            ],
            options={
                'verbose_name': 'Nova senha',
                'verbose_name_plural': 'Novas senhas',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, serialize=False, primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL)),
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
            field=models.ManyToManyField(related_query_name='user', blank=True, related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', blank=True, related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', to='auth.Permission'),
        ),
    ]
