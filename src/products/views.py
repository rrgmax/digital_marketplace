import os

from django.conf import settings
from django.urls import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from digitalmarket.mixins import (
            LoginRequiredMixin,
            MultiSlugMixim,
            SubmitBtnMixin
            )
from wsgiref.util import FileWrapper

from .forms import ProductAddForm, ProductModelForm
from .mixins import ProductManagerMixin
from .models import Product




class ProductCreateView(LoginRequiredMixin, SubmitBtnMixin ,CreateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    #success_url = "/products/"
    submit_btn = "Add"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        return valid_data

    # def get_success_url(self):
    #     return reverse("products:list")


class ProductUpdateView(ProductManagerMixin, SubmitBtnMixin, MultiSlugMixim, UpdateView):
    model = Product
    template_name = "form.html"
    form_class = ProductModelForm
    #success_url = "/products/"
    submit_btn = "Update"

    # def get_success_url(self):
    #     return reverse("product_list_view")

class ProductDetailView(MultiSlugMixim, DetailView):
    model = Product

class ProductDownloadView(MultiSlugMixim, DetailView):
    model = Product
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
        #wrapper = FileWrapper(filepath) #, blksize=5) Get AttributeError: 'str' object has no attribute 'read' 
        response = HttpResponse(filepath, content_type='application/force-download')
        response["Content-Disposition"] = "attachment; filename=%s" %(obj.media.name)
        response["X-SendFile"] = str(obj.media.name) 
        return response

class ProductListView(ListView):
    model = Product
    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        return qs

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print (form.cleaned_data.get("publish"))
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
            "form":form,
            "submit_btn": "Create"
        }
    return render(request, template, context)    

def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "object": product,
        "form": form,
        "submit_btn": "Update"
        }
    return render(request, template, context)



def detail_slug_view(request, slug=None):
    product = Product.objects.get(slug=slug)
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultupleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()    
    template = "detail_view.html"
    context = {
        "object": product
        }
    return render(request, template, context)

def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product
        }
    return render(request, template, context)


def list_view(request):
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)