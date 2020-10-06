from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'date_added', 'price')


class InvoiceSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id', 'product', 'date_ordered', 'status', 'discount', 'total'
        )
        read_only_fields = (
            'product', 'date_ordered', 'status', 'price', 'discount', 'total'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 'product', 'product_name', 'date_ordered', 'status', 'price', 'discount', 'total'
        )
        read_only_fields = (
            'product', 'date_ordered', 'status', 'price', 'discount', 'total', 'product_name'
        )


class OrderEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id', 'product', 'product_name', 'date_ordered', 'status', 'price', 'discount', 'total'
        )
        read_only_fields = (
            'date_ordered', 'status', 'price', 'discount', 'total', 'product_name'
        )
