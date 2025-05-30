from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    category=models.CharField(max_length=100)
    price=models.FloatField()
    discounted_price=models.FloatField()
    image=models.ImageField(default='default.jpg',upload_to='imgs/')
    buyer_count = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    email=models.TextField(max_length=500)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)

 


class Users_Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    image = models.ImageField(upload_to="shop/images", default="")
    link = models.URLField(max_length=200, blank=True, null=True)  # <--- this is your link field

    def __str__(self):
        return self.title


