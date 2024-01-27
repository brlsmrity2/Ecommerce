from .views import (
    SearchProductView
)
from django.urls import path


app_name = 'search'


urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
