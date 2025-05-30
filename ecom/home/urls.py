from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from shop import views as views2
from . import views 

app_name='home'
urlpatterns = [
    path('',views.main,name='main'),
    path('home/',views.home,name='home'),
    # path('shop/',views2.index, name='index'),
    path('cabinet/',views.user_Data,name='cabinet'),
    path('login/',views.login_page,name='login_page'),
     path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name='logout_page'),
    path('collaboration/',views.collaboration,name='collaboration'),
    path('collaborate/',views.collaborate,name='collaborate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)