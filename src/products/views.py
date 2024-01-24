
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Product

# Create your views here.


# CLASS BASED

class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'


class ProductListView(ListView):
    model = Product
    querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(
    #         *args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = super().get_queryset()
        return Product.objects.all()


class ProductDetailSlugView(DetailView):
    model = Product
    querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("hmmm??")
        return instance


class ProductDetailView(DetailView):
    # model = Product
    # querySet = Product.objects.all()  # get all the products from model Product
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesnot exit")
        return instance
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)

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
    # try:
    #     instance = get_object_or_404(Product, pk=pk)
    #     context = {"object": instance}
    #     return render(request, "products/detail.html", context)
    # except Http404:
    #     return render(request, "products/404.html", {"error_message": "No product found matching the query"}, status=404)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No Product Here')
    #     raise Http404('Product doesn\'t exit')
    # except:
    #     print('HUH?')
    instance = Product.objects.get_by_id(pk)
    # print(instance)
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Not Found")
    if instance is None:
        raise Http404('Product doesn\'t exit')
    context = {"object": instance}
    return render(request, "products/detail.html", context)
