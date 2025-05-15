from django.shortcuts import render, redirect
from .models import Products,Order
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import json
from datetime import datetime



@login_required(login_url='home:login_page')

def index(request):
    # if request.user.is_anonymous:
    #     return redirect('home:login_page')
    print("User is authenticated:", request.user.is_authenticated)
    prod = Products.objects.all()

    item = request.GET.get('item_name')
    category = request.GET.get('category')

    if item and item != '':
        prod = prod.filter(title__icontains=item)

    if category and category != '':
        prod = prod.filter(category__iexact=category)

    return render(request, 'shop/index.html', {'products': prod})

def logout_page(request):
    logout(request)
    return redirect('home:login_page') 
def details(request,id):
    prod=Products.objects.get(id=id)
    return render(request,'shop/details.html',{'product':prod})

def checkout(request):
    if request.method=="POST":
        items=request.POST.get("items","")
        name=request.POST.get("name","") #2nd is the default val
        email=name=request.POST.get("email","")
        address=request.POST.get("address","")
        city=request.POST.get("city","")
        state=name=request.POST.get("state","")
        zipcode=request.POST.get("zipcode","")
        total=request.POST.get("total","")

        order=Order(items=items,name=name,email=email, address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
        items_dict = json.loads(items)
         

        current_datetime = datetime.now().strftime('%B %d, %Y %I:%M %p')  # example: May 14, 2025 09:27 PM

        # Load template
        template = loader.get_template('shop/invoice.html')

        # Render template to HTML
        html = template.render({
            'order': order,
            'items': items_dict,
            'current_date': current_datetime
            })
        options={
            'page-size':'letter',
            'encoding':'UTF-8',
             'enable-local-file-access': None,
        }
        # Generate PDF
        pdf=pdfkit.from_string(html,False,options)
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Invoice_{order.id}.pdf"'
        

        return response

    return render(request,'shop/checkout.html')

