from django.shortcuts import render

from .models import Phone

phone_data = Phone.objects.all()


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort', 'name'):
        phone_data.order_by("name")
    elif request.GET.get('sort', 'min_price'):
        phone_data.order_by("-price")
    elif request.GET.get('sort', 'max_price'):
        phone_data.order_by("price")
    context = {'phone_data': phone_data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    slug = Phone.slug(phone_data.get('name'))
    context = {}
    return render(request, template, context)
