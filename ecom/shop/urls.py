from django.contrib import admin
from django.urls import path
from . import views as views1
from home import views as views2 
app_name='shop'
urlpatterns = [
   
    path('',views1.index,name='index'),
    
    path('detail/<int:id>/',views1.details,name='detail'),
    path('shop/checkout/',views1.checkout, name='checkout'),
]
