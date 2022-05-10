from audioop import reverse
from pickle import NONE
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.db.models import *
from django.contrib.auth.decorators import login_required

@login_required 
def add_to_cart(request):
    user = request.user
    product = Product.objects.get(id=request.POST['product'])
    if Cart.objects.filter(product=product, customer=user).exists():
        cart = Cart.objects.get(product=product, customer=user)
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart() 
        cart.customer = user
        cart.quantity = 1
        cart.product = product
        cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required 
def service_add_to_cart(request):
    user = request.user
    service = Service.objects.get(id=request.POST['service'])
    if Cart.objects.filter(service=service, customer=user).exists():
        cart = Cart.objects.get(service=service, customer=user)
        cart.quantity += 1
        cart.save()
    else:
        cart = Cart() 
        cart.customer = user
        cart.quantity = 1
        cart.service = service
        cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def item(request, item_id):
    item = Product.objects.get(id=item_id)
    return render(request, 'item.html', {"product":item})

def service_item(request, item_id):
    item = Service.objects.get(id=item_id)
    return render(request, 'service_item.html', {"service":item})

def is_valid_param(param):
    return param != '' and param is not None

def products(request):
    context = {}
    context["types"] = ProductType.names
    context["brands"] = Product.objects.order_by().values_list('brand', flat=True).distinct()
    context["vendors"] = Vendor.objects.order_by().values_list('name', flat=True).distinct()
    context["max_price"] = Product.objects.all().aggregate(Max('price'))
    context["min_price"] = Product.objects.all().aggregate(Min('price'))
    context["sizes"] = Product.objects.order_by('size').values_list('size', flat=True).distinct()
    max_price = request.POST.get("max_price")
    min_price = request.POST.get("min_price")
    
    if request.POST.get('View', None):
        context["product"] = Product.objects.filter(id=request.POST.get("product"))
        return HttpResponseRedirect(reverse('item', args=(id,)), context)
    
    filters = {
        key: value
        for key, value in request.POST.items()
        if key in ['brand', 'type', 'size'] and value != ""
    }
    
    vendor = request.POST.get('vendor')
    if is_valid_param(vendor):
        filters['vendor'] = Vendor.objects.get(name=vendor).id

    query_name = request.POST.get('name', None)
    if (query_name == None):
        query_name = ""
    
    qs = Product.objects.filter(name__contains=query_name, **filters)
    if is_valid_param(max_price):
        qs = qs.filter(price__lte=max_price)
        
    if is_valid_param(min_price):
        qs = qs.filter(price__gt=min_price)
        
    context["products"] = qs
    return render(request, 'products.html', context)

def purchase(request):
    Cart.objects.filter(customer=request.user.id).delete()
    return render(request, 'purchase.html')

@login_required 
def cart(request):
    product = request.POST.get("product")
    service = request.POST.get("service")
    if product != None:
        Cart.objects.filter(customer=request.user, product=product).delete()
    if service != None:
        Cart.objects.filter(customer=request.user, service=service).delete()

    results = Cart.objects.filter(customer=request.user.id)
    total = 0
    for item in results:
        if item.product is not None:
            total += (item.product.price * item.quantity)
        if item.service is not None:
            total += (item.service.price * item.quantity)
    return render(request, 'cart.html', {"cart":results, "total":total})

def services(request):
    context = {}
    context["vendors"] = Vendor.objects.order_by().values_list('name', flat=True).distinct()
    context["max_bandwidth"] = Service.objects.all().aggregate(Max('bandwidth'))
    context["min_bandwidth"] = Service.objects.all().aggregate(Min('bandwidth'))
    context["max_price"] = Service.objects.all().aggregate(Max('price'))
    context["min_price"] = Service.objects.all().aggregate(Min('price'))
    max_bandwidth = request.POST.get("max_bandwidth")
    min_bandwidth = request.POST.get("min_bandwidth")
    max_price = request.POST.get("max_price")
    min_price = request.POST.get("min_price")
    
    if request.POST.get('View', None):
        context["service"] = Service.objects.filter(id=request.POST.get("service"))
        return HttpResponseRedirect(reverse('item', args=(id,)), context)
    
    filters = {
        key: value
        for key, value in request.POST.items()
        if key in [] and value != ""
    }
    
    vendor = request.POST.get('vendor')
    if is_valid_param(vendor):
        filters['vendor'] = Vendor.objects.get(name=vendor).id

    query_name = request.POST.get('name', None)
    if (query_name == None):
        query_name = ""

    qs = Service.objects.filter(name__contains=query_name, **filters)
    if is_valid_param(max_price):
        qs = qs.filter(price__lte=max_price)
    if is_valid_param(min_price):
        qs = qs.filter(price__gt=min_price)
    if is_valid_param(max_bandwidth):
        qs = qs.filter(bandwidth__lte=max_bandwidth)
    if is_valid_param(min_bandwidth):
        qs = qs.filter(bandwidth__gt=min_bandwidth)

    context["services"] = qs
    return render(request, 'services.html', context)

def vendors(request):
    context = {}
    
    if request.POST.get('View', None):
        context["vendor"] = Vendor.objects.filter(id=request.POST.get("vendor"))
        return HttpResponseRedirect(reverse('item', args=(id,)), context)
    
    filters = {
        key: value
        for key, value in request.POST.items()
        if key in [] and value != ""
    }

    query_name = request.POST.get('name', None)
    if (query_name == None):
        query_name = ""

    qs = Vendor.objects.filter(name__contains=query_name, **filters)

    context["vendors"] = qs
    return render(request, 'vendors.html', context)
