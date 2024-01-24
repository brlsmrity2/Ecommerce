from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='Products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(),
         name='ProductDetail'),
    path('products/fnc/', views.product_list_view, name='product_list'),
    path('products/fnc/<int:pk>/', views.product_detail_view, name='product_detail'),
    # Other app1 URLs
]