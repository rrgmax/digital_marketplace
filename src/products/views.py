from django.shortcuts import render

from .models import Product

# Create your views here.
def detail_view(request):
    product = Product.objects.all().first()
    template = "detail_view.html"
    context = {
        "title": "Hello Again",
        "product": product
    }
    return render(request, template, context)

def list_view(request):
    template = "detail_view.html"
    context = {}
    return render(request, template, context)