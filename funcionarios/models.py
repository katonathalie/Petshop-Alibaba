import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core import validators


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome de usuário', max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail', unique=True, blank=False)
    name = models.CharField('Nome completo', max_length=100, blank=False, validators=[validators.RegexValidator(re.compile('^[a-zA-Z ]+$'),
            'Nome completo só pode conter letras', 'invalid')])
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    password1 = models.CharField('', max_length=30)
    password2 = models.CharField('Confirmação de Senha', max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # field de login
    REQUIRED_FIELDS = ['username']  # criacao de super user

    def __str__(self):
        return self.name

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['name']

