from django.db import models

from drink.models import Drink
from user.models import User


class Sale(models.Model):
    user = models.ForeignKey(User, verbose_name='Продавец', on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, verbose_name='Напиток', related_name='drink', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    @property
    def user_name(self):
        return self.user.username

    @property
    def drink_name(self):
        return self.drink.name

    @property
    def price(self):
        return self.drink.price

    @property
    def price_total(self):
        return self.drink.price * self.quantity
