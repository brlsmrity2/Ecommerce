from typing import Any
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



from .models import Product

# Create your views here.


# CLASS BASED

class ProductListView(ListView):
    model = Product
    querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context


class ProductDetailView(DetailView):
    model = Product
    querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj is None:
            raise Http404("No product found matching the query")
        return obj


# Function Based

def product_list_view(request):
    querySet = Product.objects.all()
    context = {
        "object_list": querySet
    }
    return render(request, "products/list.html", context)


# def product_detail_view(request, pk=None, *args, **kwargs):
#     # instance = Product.objects.get(pk=pk)
#     instance = get_object_or_404(Product, pk=pk)
#     context = {
#         "object": instance
#     }
#     return render(request, "products/detail.html", context)
def product_detail_view(request, pk=None, *args, **kwargs):
    try:
        instance = get_object_or_404(Product, pk=pk)
        context = {"object": instance}
        return render(request, "products/detail.html", context)
    except Http404:
        return render(request, "products/404.html", {"error_message": "No product found matching the query"}, status=404)
