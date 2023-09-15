from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email-адрес')

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    # Верификация почты пользователя
    code_verification = models.CharField(max_length=20, verbose_name='Код верификации', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='Проверка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
