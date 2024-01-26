from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('featured/', views.ProductFeaturedListView.as_view(),
         name='FeaturedProducts'),
    path('featured/<int:pk>/', views.ProductFeaturedDetailView.as_view(),
         name='FeaturedProduct'),
    path('', views.ProductListView.as_view(), name='Products'),
    path('<int:pk>/', views.ProductDetailView.as_view(),
         name='ProductDetail'),
    path('<slug:slug>/',
         views.ProductDetailSlugView.as_view(), name='ProductSlug'),
    path('fnc/', views.product_list_view, name='product_list'),
    path('products/fnc/<int:pk>/', views.product_detail_view, name='product_detail'),
    # Other app1 URLs
]
