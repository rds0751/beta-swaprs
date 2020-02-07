
from django.db import models
from django.contrib.auth.models import User

from src.products.models import Product

# Create your models here.

class UserPurchase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    
    def __unicode__(self, ):
        return self.user.username
    
    