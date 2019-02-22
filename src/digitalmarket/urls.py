from django.contrib import admin
from django.urls import path, re_path
from products.views import ProductListView
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('create/', views.create_view, name="create_view"),
    re_path('detail/(?P<object_id>\d+)/edit/$', views.update_view, name="update_view"),
    re_path('detail/(?P<object_id>\d+)/$', views.detail_view, name="detail_view"),
    re_path('detail/(?P<slug>[\w-]+)/$', views.detail_slug_view, name="detail_slug_view"),
    re_path('list/', views.list_view, name="list_view"),
    re_path('products/list/$', ProductListView.as_view(), name="product_list_view"),
]
