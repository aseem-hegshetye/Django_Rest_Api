from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import JsonResponse
from .models import *


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    print('product_detail')
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'product': {
                'name': product.name,
                'manufacturer': product.manufacturer.name,
                'photo': product.photo.url
            }
        }
        response = JsonResponse(data, status=201)
    except:
        data = {
            'error': {
                'code': 404,
                'message': 'product not found'
            }
        }

        response = JsonResponse(data, status=404)

    return response


def manufacturer_detail(request, id):
    """ django view as API"""
    manu = Manufacturer.objects.get(pk=id)
    print(f'products={list(manu.products.values())}')
    data = {
        'name': manu.name,
        'location': manu.location,
        'active': manu.active,
        'products': list(manu.products.values('name'))
    }
    return JsonResponse(data, status=201)


def manufacturer(request):
    """list all manufacturers"""
    manu = Manufacturer.objects.filter(active=True)
    data = {'manu':list(manu.values())}
    return JsonResponse(data,status=201)
