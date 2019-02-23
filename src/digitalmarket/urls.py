from django.contrib import admin
from django.urls import path, re_path
from products import views
from products.views import (
    ProductCreateView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('create/', views.create_view, name="create_view"),
    re_path('detail/(?P<object_id>\d+)/edit/$', views.update_view, name="update_view"),
    re_path('detail/(?P<object_id>\d+)/$', views.detail_view, name="detail_view"),
    re_path('detail/(?P<slug>[\w-]+)/$', views.detail_slug_view, name="detail_slug_view"),
    re_path('list/', views.list_view, name="list_view"),
    re_path('products/$', ProductListView.as_view(), name="product_list_view"),
    re_path('products/add/$', ProductCreateView.as_view(), name="product_create_view"),
    re_path('products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name="product_detail_view"),
    re_path('products/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name="product_detail_slug_view"),
    re_path('products/(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name="product_update_view"),
    re_path('products/(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name="product_update_view"),        
]
