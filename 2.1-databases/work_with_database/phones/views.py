from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort != '':
        param = request.GET.get('sort')
        if param == 'name':
            phones_objects = Phone.objects.order_by(param)
        elif param == 'min_price':
            phones_objects = Phone.objects.order_by('price')
        elif param == 'max_price':
            phones_objects = Phone.objects.order_by('-price')
    else:
        phones_objects = Phone.objects.all()
    context = {'phones':phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone':phone}
    return render(request, template, context)
