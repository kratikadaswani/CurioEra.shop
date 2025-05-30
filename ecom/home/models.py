from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# def user_data(Models.model)
class Products(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    category=models.CharField(max_length=100)
    price=models.FloatField()
    discounted_price=models.FloatField()
    image=models.ImageField(default='default.jpg',upload_to='imgs/')

class Users_data(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    desc=models.TextField(max_length=500)
    image=models.ImageField(upload_to='user_imgs/')
    userid=models.CharField(max_length=100)

    def __str__(self):
        return self.userid

class Tweet(models.Model):
    username = models.CharField(max_length=50)
    comment = models.TextField()
    image = models.ImageField(upload_to='tweets/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username