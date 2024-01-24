from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='Products'),
    path('products/fnc/', views.product_list_view, name='product_list'),
    # Other app1 URLs
]
