from django.db import models


class Product(models.Model):
    """
    Товар в PIM-системе.
    """
    sku = models.CharField(max_length=100, unique=True, verbose_name='Артикул',
                           help_text='Уникальный идентификатор товара', )
    name = models.CharField(max_length=255, verbose_name='Название', )
    description = models.TextField(blank=True, verbose_name='Описание', )
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена', )
    category = models.CharField(max_length=100, blank=True,
                                verbose_name='Категория', )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создан', )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлён', )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        indexes = [
            models.Index(fields=['sku']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f'{self.sku} — {self.name}'
