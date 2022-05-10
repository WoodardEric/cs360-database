from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Customer

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customer
    list_display = ["email", "username", 'address', 'city', 'state', 'phone']

admin.site.register(Customer, CustomUserAdmin)