from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from shop import views as views2
from . import views 

app_name='home'
urlpatterns = [
    path('',views.home,name='home'),
    # path('shop/',views2.index, name='index'),
    path('cabinet/',views.user_Data,name='cabinet'),
    path('login/',views.login_page,name='login_page'),
     path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name='logout_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)