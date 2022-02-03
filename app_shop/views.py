from django.shortcuts import render
from .models import Product, Tag
from django.core.paginator import Paginator


def home(request):
    ctx = {
        'product_list': Product.objects.all()
    }
    return render(request, 'home.html', ctx)

def product_detail(request, pk):
    ctx = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'product_detail.html', ctx)


def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3) # Show 3 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ctx = {
        'product_list': Product.objects.all(),
        'tag_list': Tag.objects.all(),
        'page_obj': page_obj
    }
    return render(request, 'product_list.html', ctx)