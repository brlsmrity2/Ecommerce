from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Product

# Create your views here.


# CLASS BASED

class ProductListView(ListView):
    model = Product
    querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/product_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context


# Function Based

def product_list_view(request):
    querySet = Product.objects.all()
    context = {
        "object_list": querySet
    }
    return render(request, "products/product_list.html", context)
