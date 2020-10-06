from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'name', 'date_added', 'price']
    # list_display = [field.name for field in Product._meta.fields]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['id', 'product_name', 'date_ordered', 'status', 'price', 'discount', 'total']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
