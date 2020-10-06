import json
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from .models import Product, Order
from dateutil.relativedelta import *
from rest_framework.test import APIClient


class OrderTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.product_test = Product.objects.create(
            name='test product', price=100.00
        )
        self.product_sale = Product.objects.create(
            name='product on sale', price=100.00,
        )
        self.product_sale.date_added -= relativedelta(months=1)
        self.product_sale.save()
        self.test_order = Order.objects.create(product=self.product_test)

    def test_order_create(self):
        res = self.client.post(
            reverse('order-create'),
            data={"product": self.product_test.id},
        )
        order_data = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(order_data['status'], 'Open')

    def test_order_discount(self):
        res = self.client.post(
            reverse('order-create'),
            data={"product": self.product_sale.id},
        )
        order_data = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertLess(0,  float(order_data['discount']))

    def test_open_order_done(self):
        res = self.client.put(
            reverse('open-order-done', kwargs={"pk": self.test_order.id}),
        )
        order_data = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(order_data['status'], 'Done')

    def test_done_order_paid(self):
        res = self.client.put(
            reverse('done-order-paid', kwargs={"pk": self.test_order.id}),
        )
        order_data = json.loads(res.content)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(order_data['status'], 'Paid')
