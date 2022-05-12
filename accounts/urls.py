from django.urls import path

from . import views 
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("customer/", views.account, name='account'),
    path("customer/unsubscribe", views.unsubscribe, name='unsubscribe'),
    path("customer/update_account", views.update_account, name='update_account'),
    path("customer/delete_account", views.delete_account, name='delete_account'),
]
