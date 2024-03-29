from django.db import models
# Create your models here.
from products.models import Product, Variations
class Cart(models.Model):
    total = models.DecimalField(max_digits=10000000, decimal_places=6, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return "Cart id : {}".format(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE )
    variations = models.ManyToManyField(Variations,null = True, blank = True)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    notes = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return self.product.title