from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)

    

    def __str__(self):
        return self.title
