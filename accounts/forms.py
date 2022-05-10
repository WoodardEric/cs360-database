from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from products.models import Customer

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ('username', 'email')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'email', 'address', 'city', 'state', 'phone')
