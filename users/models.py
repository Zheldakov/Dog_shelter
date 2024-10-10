# Описание моделей
from django.db import models
from django.contrib.auth.models import  AbstractUser

# настройка полей, чтобы возможно было заполнить поля пустыми
NULLABLE ={'blank': True, 'null': True}

class User(AbstractUser):
    """Модель пользователя с полями email, телефон и Telegram username."""
    username = None
    email = models.EmailField(unique=True,verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='telephone_number', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram_username', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active', help_text='Активный пользователь')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return  f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural ='User'
        ordering = ['id']