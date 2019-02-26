from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.text import slugify

def download_media_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers_products", blank=True)    
    media = models.FileField(blank=True, null=True, upload_to=download_media_location, storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99, null=True, blank=True)

 
    def __str__(self):
        return self.title

    def get_absolut_url(self):
        view_name = "products:detail_slug"
        return reverse(view_name, kwargs={"slug": self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug        
    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug        


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)
