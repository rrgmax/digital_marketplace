from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99, null=True, blank=True)

 
    def __str__(self):
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_reciever, sender=Product)
