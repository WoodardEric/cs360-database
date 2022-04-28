from audioop import reverse
from itertools import product
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
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

def products(request):
    if request.POST.get('View', None):
        item = Product.objects.filter(id=request.POST.get("product"))
        return HttpResponseRedirect(reverse('item', args=(id,)), {"product":item})
    elif request.POST.get('addCart', None):
        query_name = request.POST.get('name', None)
        results = Product.objects.filter(name__contains=query_name)
        return render(request, 'products.html', {"products":results})
    else:
        context = {}
        context["products"] = Product.objects.all(); 
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
    
