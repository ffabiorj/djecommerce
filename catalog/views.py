from django.shortcuts import render

# Create your views here.

from .models import Product, Category


def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/products.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'products': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
