from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - ${self.price} - {self.description}'
