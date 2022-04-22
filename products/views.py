from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

@login_required 
def add_to_cart(request):
    cart = Cart()
    cart.customer = request.user
    cart.quantity = 1
    cart.product = Product.objects.get(id=request.POST['product']) 
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def index(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        results = Product.objects.filter(name__contains=query_name)
        return render(request, 'products.html', {"products":results})
    else:
        context = {}
        context["products"] = Product.objects.all(); 
        return render(request, 'products.html', context)

@login_required 
def cart(request):
    product = request.POST.get("product")
    if product != None:
        Cart.objects.filter(customer=request.user, product=product).delete()

    results = Cart.objects.filter(customer=request.user.id)
    return render(request, 'cart.html', {"cart":results})
    
