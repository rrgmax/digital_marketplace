from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=99.99, null=True, blank=True)

 
    def __str__(self):
        return self.title
