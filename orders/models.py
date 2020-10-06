import decimal
from django.db import models
from dateutil.relativedelta import *
from django_filters import rest_framework as filters


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Done', 'Done'),
    ('Paid', 'Paid'),
)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, )
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Open', choices=STATUS_CHOICES, max_length=10)

    @property
    def price(self):
        return self.product.price

    @property
    def discount(self):
        return round(self.price * decimal.Decimal(0.2), 2) if self.do_discount() else decimal.Decimal(0)

    @property
    def total(self):
        return round(self.price - self.discount, 2)

    @property
    def product_name(self):
        return self.product.name

    def do_discount(self):
        return self.product.date_added + relativedelta(months=1) < self.date_ordered

    def __str__(self):
        return f'{self.date_ordered} {self.product_name}'


class OrderFilter(filters.FilterSet):
    date_ordered = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        fields = ['date_ordered', 'status']
