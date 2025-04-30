from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    category=models.CharField(max_length=100)
    price=models.FloatField()
    discounted_price=models.FloatField()
    image=models.ImageField(default='default.jpg',upload_to='imgs/')


class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=100)
    email=models.TextField(max_length=500)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.PositiveIntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
