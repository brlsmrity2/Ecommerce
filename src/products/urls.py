from django.urls import path
from . import views

urlpatterns = [
    path('featured/', views.ProductFeaturedListView.as_view(),
         name='FeaturedProducts'),
    path('featured/<int:pk>/', views.ProductFeaturedDetailView.as_view(),
         name='FeaturedProducts'),
    path('products/', views.ProductListView.as_view(), name='Products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(),
         name='ProductDetail'),
    path('products/<slug:slug>/',
         views.ProductDetailSlugView.as_view(), name='ProductSlug'),
    path('products/fnc/', views.product_list_view, name='product_list'),
    path('products/fnc/<int:pk>/', views.product_detail_view, name='product_detail'),
    # Other app1 URLs
]
