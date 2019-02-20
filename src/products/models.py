from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=None, decimal_places=None)
    
    

    def __str__(self):
        return self.title
