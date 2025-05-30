from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Products,Users_data,Tweet
from shop.models import Users_Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import Users_Product
from .forms import UserProductForm,TweetForm
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


from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check for existing email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('home:register')

        # Check for existing username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
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


def main(request):
    return render(request, 'home/main.html')

from django.shortcuts import render, redirect
from django.conf import settings
import os
from django.contrib import messages


@login_required(login_url='home:login_page')
def user_Data(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None)
        desc = request.POST.get('desc', "")

        if image and desc:
            user_imgs_path = os.path.join(settings.MEDIA_ROOT, 'user_imgs')
            if not os.path.exists(user_imgs_path):
                os.makedirs(user_imgs_path)

            user = Users_data(
                image=image,
                desc=desc,
                userid=request.user.username  # Attach logged-in username here
            )
            user.save()

            messages.success(request, 'Your memory has been added to the wall!✨')
            return redirect('home:cabinet')

        else:
            messages.error(request, 'Please make sure to upload an image and share your story.')
            return redirect('home:cabinet')

    data = Users_data.objects.all()
    return render(request, "home/cabinet.html", {'data': data})


@login_required
def collaborate(request):
    user = request.user
    products = Users_Product.objects.filter(user=user)

    action = request.GET.get('action', 'add')  # 'add' or 'update'
    prod_id = request.GET.get('prod_id')

    if action == 'update' and prod_id:
        product = get_object_or_404(Users_Product, id=prod_id, user=user)
        form = UserProductForm(request.POST or None, request.FILES or None, instance=product)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('home:collaboration')
    elif action == 'add':
        form = UserProductForm(request.POST or None, request.FILES or None)
        if request.method == "POST" and form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = user
            new_product.save()
            return redirect('home:collaboration')
    else:
        form = None

    context = {
        'products': products,
        'form': form,
        'action': action,
        'prod_id': prod_id
    }

    return render(request, 'shop/collaborate.html', context)



@login_required(login_url='home:login_page')
@login_required(login_url='home:login_page')


@login_required(login_url='home:login_page')
def collaboration(request):
    form = TweetForm()  # default form

    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        # Handling product submissions
        if form_type == 'add_prod':
            brand_name = request.POST.get("brand_name", "")
            title = request.POST.get("title", "")
            desc = request.POST.get("desc", "")
            category = request.POST.get("category", "")
            price = request.POST.get("price", "")
            discounted_price = request.POST.get("discounted_price", "")
            image = request.FILES.get("image", "")
            user_id = request.POST.get("user_id", "")

            if title and category and price and image and user_id:
                product = Users_Product(
                    brand_name=brand_name,
                    title=title,
                    desc=desc,
                    category=category,
                    price=price,
                    discounted_price=discounted_price,
                    image=image,
                    user_id=request.user.username
                )
                product.save()

        # Handling tweet submissions
        elif form_type == 'tweet':
            form = TweetForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home:collaboration')

    # On GET: fetch products & tweets
    prod = Users_Product.objects.all()
    posts = Tweet.objects.all().order_by('-created_at')

    return render(request, 'home/collaboration.html', {'data': prod, 'form': form, 'posts': posts,'userid':request.user.username})


