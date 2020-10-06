"""OrderDiscount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from orders import api_views

schema_view = get_schema_view(
   openapi.Info(
      title="Orders API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@test_orders.test"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('product-list/', api_views.ProductList.as_view(), name='product-list'),
    path('order-cteate/', api_views.CashierOrderCreateView.as_view(), name='order-create'),
    path('open-orders/', api_views.OpenOrderList().as_view(), name='open-order-list'),
    path('accountant-order-list/', api_views.AccountantOrderList().as_view(), name='accountant-order-list'),
    path('open-order-done/<int:pk>/', api_views.OpenOrderDone.as_view(), name='open-order-done'),
    path('done-order-paid/<int:pk>/', api_views.DoneOrderPaid.as_view(), name='done-order-paid'),
    path('order-invoice/<int:pk>/', api_views.OrderInvoice.as_view(), name='order-invoice'),
]
