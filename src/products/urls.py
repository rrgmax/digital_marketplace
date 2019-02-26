from django.contrib import admin
from django.urls import path #, re_path
from .views import (
    ProductCreateView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    )

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('add/', ProductCreateView.as_view(), name="create"),
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('<slug:slug>/', ProductDetailView.as_view(), name="detail_slug"),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="update"),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name="update_slug"),
    # re_path('(?P<pk>\d+)/$', ProductDetailView.as_view(), name="detail"),
    # re_path('(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name="detail_slug"),
    # re_path('(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name="update"),
    # re_path('(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name="update_slug"),        
]
