from .serializers import ProductSerializer, OrderSerializer, InvoiceSerializer, OrderEditSerializer
from .models import Order, Product, OrderFilter
from rest_framework import generics


class ProductList(generics.ListAPIView):
    """
    Return a list of the products
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# todo check cashier permissions
class CashierOrderCreateView(generics.CreateAPIView):
    """
    Create order for given product_id. Sample data: {"product": 6}
    """
    queryset = Order.objects.all()
    serializer_class = OrderEditSerializer


# todo check cashier permissions
class OpenOrderList(generics.ListAPIView):
    """
    Return a list of the orders with status 'Open'
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(status='Open')


# todo check accountant permissions
class AccountantOrderList(generics.ListAPIView):
    """
    Return a (filtered) list of orders
    example: GET /accountant-orders/?date_ordered_after=2020-10-02&date_ordered_before=&status=Done
    Parameters:
        - status: ['Open', 'Done', 'Paid']
        - date_ordered_after: <date-time>
        - date_ordered_before: <date-time>
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filterset_class = OrderFilter


# todo check sales permissions
class OpenOrderDone(generics.UpdateAPIView):
    """
    Sets the status 'Done' for the order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        serializer.validated_data['status'] = 'Done'
        serializer.save()


# todo check accountant permissions
class DoneOrderPaid(generics.UpdateAPIView):
    """
    Sets the status 'Paid' for the order
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_update(self, serializer):
        serializer.validated_data['status'] = 'Paid'
        serializer.save()
