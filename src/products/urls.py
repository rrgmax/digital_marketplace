from django.contrib import admin
from django.urls import path #, re_path
from .views import (
    ProductCreateView,
    ProductDetailView,
    ProductDownloadView,
    ProductListView,
    ProductUpdateView,
    )

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('add/', ProductCreateView.as_view(), name="create"),
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('<slug:slug>/', ProductDetailView.as_view(), name="detail_slug"),
    path('<int:pk>/download/', ProductDownloadView.as_view(), name="download"),
    path('<slug:slug>/download/', ProductDownloadView.as_view(), name="download_slug"),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name="update"),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name="update_slug"),
 ]
