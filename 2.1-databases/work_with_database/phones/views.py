from django.shortcuts import render, redirect
from .models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        res = phones.order_by('name')
    elif sort == 'min_price':
        res = phones.order_by('price')
    elif sort == 'max_price':
        res = phones.order_by('-price')
    else:
        res = phones


    context = {'phones': res}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slugs = Phone.objects.get(slug=slug)

    context = {'phone':  slugs}
    return render(request, template, context)
