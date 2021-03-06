from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth import logout
from products.models import History
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def account(request):
    context = {}
    context['history'] = History.objects.filter(customer=request.user)
    return render(request, 'account.html', context)

def update_account(request):
    customer = request.user
    customer.username = request.POST.get('inputUser')
    customer.email = request.POST.get('inputEmail')
    customer.Address = request.POST.get('inputAddress')
    customer.city = request.POST.get('inputCity')
    customer.state = request.POST.get('inputState')
    customer.phone = request.POST.get('inputPhone')
    customer.save()
    return render(request, 'home.html')

def delete_account(request):
    user  = request.user
    logout(request)
    user.delete()
    return render(request, 'home.html')

@login_required 
def unsubscribe(request):
    user = request.user
    if user.service != None:
        user.service = None
        user.save()
    return render(request, "home.html")
