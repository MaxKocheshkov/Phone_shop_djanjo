from django.shortcuts import render, get_object_or_404

from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    if 'name' in request.GET.get('sort'):
        n_context = {'phone_data': Phone.objects.all().order_by("name")}
        return render(request, template, context=n_context)
    elif 'min_price' in request.GET.get('sort'):
        min_context = {'phone_data': Phone.objects.all().order_by("price")}
        return render(request, template, context=min_context)
    elif 'max_price' in request.GET.get('sort'):
        max_context = {'phone_data': Phone.objects.all().order_by("-price")}
        return render(request, template, context=max_context)
    else:
        context = {'phone_data': Phone.objects.all()}
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    product_data = get_object_or_404(Phone, slug=slug)
    context = {'product_data': product_data}
    return render(request, template, context=context)
