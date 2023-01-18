from django.contrib import admin

from store.models import Product, Order, Cart


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'description',)
    list_filter = ('name', 'price', 'stock',)
    list_display_links = ('name',)
    list_editable = ('price', 'stock',)
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'ordered', 'user',)
    list_per_page = 20


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # list_editable = ('user',)
    # list_display_links = ('user',)
    list_per_page = 20
