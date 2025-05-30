from django.shortcuts import render, redirect
from .models import Products,Order,Users_Product
from django.contrib.auth import authenticate,login,logout
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import json
from datetime import datetime
from django.core.mail import send_mail


@login_required(login_url='home:login_page')

def index(request):
    prod = Products.objects.all()
    

    products = list(prod) 

    item = request.GET.get('item_name')
    category = request.GET.get('category')

    if item and item != '':
        products = [p for p in products if item.lower() in p.title.lower()]

    if category and category != '':
        products = [p for p in products if p.category.lower() == category.lower()]

    return render(request, 'shop/index.html', {'products':products})


def logout_page(request):
    logout(request)
    return redirect('home:login_page') 
def details(request,id):
    prod=Products.objects.get(id=id)
    return render(request,'shop/details.html',{'product':prod})

from django.shortcuts import render, redirect, get_object_or_404
# from .models import Users_Product
# from .forms import UserProductForm
from django.contrib.auth.decorators import login_required




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

        #numb of buyers
        items_dict = json.loads(items)

        # If it's a string, decode again
        for item in items_dict:
         if isinstance(item, dict):
            product_id = item.get('id')
            if product_id:
                try:
                    product = Products.objects.get(id=product_id)
                    product.buyers_count += 1
                    product.save()
                except Products.DoesNotExist:
                    pass
        else:
            print(f"Skipping invalid item: {item}")

            
        #pdf gen
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
        email_subject = 'Order Confirmation - Curio’s Vintage Collection'
        email_body = 'Thank you for your purchase! Your order has been placed successfully. Attached is your invoice.'

        message = EmailMessage(
            email_subject,
            email_body,
            'your_email@gmail.com',  # from email
            [email],                 # to email
        )

        message.attach(f'Invoice_{order.id}.pdf', pdf, 'application/pdf')

        message.send(fail_silently=False)


        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Invoice_{order.id}.pdf"'
        
        return response

    return render(request,'shop/checkout.html')


