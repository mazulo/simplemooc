from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)
from django.core import validators
from django.conf import settings
import re


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuário',
        max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'O nome de usuário só pode conter letras, números e @/./+/-/_',
                'invalid'
            )
        ]
    )
    email = models.EmailField(
        'E-mail',
        unique=True
    )
    name = models.CharField(
        'Nome',
        max_length=100,
        blank=True
    )
    is_active = models.BooleanField(
        'Está ativo?',
        blank=True,
        default=True
    )
    is_staff = models.BooleanField(
        'É da equipe?',
        blank=True,
        default=False
    )
    date_joined = models.DateTimeField(
        'Data de entrada',
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        if self.is_professor:
            return 'Professor {} '.format(self.name or self.username)
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    @property
    def is_professor(self):
        return hasattr(self, 'professor')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Professor(User):

    def __str__(self):
        return 'Professor - {}'.format(self.name or self.username)

    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'


class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário para recuperação de senha',
        related_name='resets'
    )
    key = models.CharField(
        'Chave',
        max_length=100,
        unique=True,
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    confirmed = models.BooleanField(
        'Confirmado?',
        default=False,
        blank=True
    )

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-created_at']
