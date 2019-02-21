from django.shortcuts import render

from .models import Product

# Create your views here.
def detail_view(request):
    if request.user.is_authenticated:
        product = Product.objects.all().first()
        template = "detail_view.html"
        context = {
            "title": "Hello Again",
            "object": product
        }
    else:    
        template = "not_found.html"
        context = {}
    return render(request, template, context)

def list_view(request):
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)