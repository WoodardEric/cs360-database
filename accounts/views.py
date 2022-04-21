from django.http import HttpResponse


def index(request):
    return HttpResponse("accounts index test")

def signup(request):
    return HttpResponse("accounts signup test")

def login(request):
    return HttpResponse("accounts login test")

def logout(request):
    return HttpResponse("accounts logout test")
