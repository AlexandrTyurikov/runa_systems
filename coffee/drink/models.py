from django.db import models


class Drink(models.Model):
    name = models.CharField(verbose_name='Название напитка', unique=True, max_length=120)
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    description = models.TextField(verbose_name='Описание напитка', null=True, blank=True)
    creation_date = models.DateTimeField('Дата и время создания', auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField('Дата и время изменения', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'
