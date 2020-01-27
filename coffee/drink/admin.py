from django.contrib import admin

from .models import Drink


class DrinkAdmin(admin.ModelAdmin):
    class Meta:
        model = Drink

    list_display = (
        'name',
        'price',
        'creation_date',
        'update_date',
    )
    list_filter = ('name',)


admin.site.register(Drink, DrinkAdmin)
