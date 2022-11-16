from django.contrib import admin
from .models import Product, Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offers, OfferAdmin)
