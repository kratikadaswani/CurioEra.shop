from django.contrib import admin
from .models import Products,Order,Users_Product
# Register your models here.


admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Users_Product)