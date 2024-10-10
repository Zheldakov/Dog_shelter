from django.db import models

# настройка полей, чтобы возможно было заполнить поля пустыми
NULLABLE ={'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='breed', **NULLABLE)
    description = models.CharField(max_length=150, verbose_name='description', **NULLABLE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breeds'