# from msilib.schema import Class
from unittest import result
from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def index(request):
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        results = Product.objects.filter(name__contains=query_name)
        return render(request, 'products.html', {"products":results})
    else:
        context = {}
        context["products"] = Product.objects.all(); 
        return render(request, 'products.html', context)


