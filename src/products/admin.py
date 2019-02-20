from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "description", "price", "sale_price"]
    search_fields = ["description", "title"]
    list_filter = ["price"]
    list_editable = ["sale_price"]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
