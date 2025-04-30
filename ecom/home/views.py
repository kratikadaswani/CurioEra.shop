from django.shortcuts import render,HttpResponse
from .models import Products,Users_data
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email')
            return redirect('home:login_page')

        user = authenticate(request, username=user_obj.username, password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('home:login_page')

        login(request, user)
        return redirect('/')

    return render(request, 'home/login_page.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('home:register')

        if username and email and password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('home:login_page')

        messages.error(request, 'All fields are required')
        return redirect('home:register')

    return render(request, 'home/register.html')

def logout_page(request):
    logout(request)
    return redirect('home:login_page')

@login_required(login_url='home:login_page')
def home(request):
    # return HttpResponse('hey')
    # if(request.user.is_anonymous):
    #  return redirect('home:login_page')
   
    prod = Products.objects.all()

    category = request.GET.get('category')
    if category and category != '':
        prod = prod.filter(category__iexact=category)
        return render(request, 'shop/index.html', {'products': prod})
    return render(request,'home/home.html')

from django.shortcuts import render, redirect
from django.conf import settings
import os

def user_Data(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None)
        desc = request.POST.get('desc', "")

        if image and desc:
            user_imgs_path = os.path.join(settings.MEDIA_ROOT, 'user_imgs')
            if not os.path.exists(user_imgs_path):
                os.makedirs(user_imgs_path)

            user = Users_data(image=image, desc=desc)
            user.save()

        # Redirect after POST
        return redirect('/')

    # Only fetch data on GET
    data = Users_data.objects.all()
    return render(request, "home/cabinet.html", {'data': data})

