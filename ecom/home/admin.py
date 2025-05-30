from django.contrib import admin
from .models import Users_data,Products,Tweet
# Register your models here.
admin.site.register(Products)
admin.site.register(Users_data)
admin.site.register(Tweet)