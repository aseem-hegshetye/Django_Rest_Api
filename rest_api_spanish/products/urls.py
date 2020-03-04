from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('manu/<int:id>/', manufacturer_detail, name='manufacturer_detail'),
    path('manu/', manufacturer, name='manufacturer_detail')
]
