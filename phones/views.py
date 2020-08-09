from django.shortcuts import render
from slugify import slugify
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort', 'name'):
        n_context = {'phone_data': Phone.objects.all().order_by("name")}
        return render(request, template, context=n_context)
    elif request.GET.get('sort', 'min_price'):
        min_context = {'phone_data': Phone.objects.all().order_by("price")}
        return render(request, template, context=min_context)
    elif request.GET.get('sort', 'max_price'):
        max_context = {'phone_data': Phone.objects.all().order_by("-price")}
        return render(request, template, context=max_context)
    else:
        context = {'phone_data': Phone.objects.all()}
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    for name in Phone.objects.values("name", flat=True):
        slug = slugify(name)
        context = {'slug': slug, 'phone_data': Phone.objects.all()}
        return render(request, template, context=context)
