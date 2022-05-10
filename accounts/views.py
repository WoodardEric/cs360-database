from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib.auth import logout
from accounts.models import Customer

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def account(request):
    return render(request, 'account.html')

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