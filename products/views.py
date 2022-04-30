from audioop import reverse
from itertools import product
from pickle import NONE
import re
import string
from django.http import HttpResponse, HttpResponseRedirect
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

def item(request, item_id):
    item = Product.objects.get(id=item_id)
    return render(request, 'item.html', {"product":item})

def is_valid_param(param):
    return param != '' and param is not None

def products(request):
    context = {}
    context["types"] = ProductType.names
    context["brands"] = Product.objects.order_by().values_list('brand', flat=True).distinct()
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
    if product != None:
        Cart.objects.filter(customer=request.user, product=product).delete()

    results = Cart.objects.filter(customer=request.user.id)
    total = 0
    for item in results:
        total += (item.product.price * item.quantity)
    return render(request, 'cart.html', {"cart":results, "total":total})
    
