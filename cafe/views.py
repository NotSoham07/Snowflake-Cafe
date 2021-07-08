from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Feedback, Product, Joinus, Orders
from math import *


def home(request):
    return render(request, 'home.html')

def feedback(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        feedback = request.POST.get('subject','')
        data = Feedback(name=name, email = email, feedback=feedback )
        data.save()
    return render(request, 'feedback.html')

def menu(request):
    #products = Product.objects.all()
    #n = len(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'menu.html', params)

def joinus(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone', '')
        location = request.POST.get('location', '')
        file = request.POST.get('file', '')
        subject = request.POST.get('subject','')
        data = Joinus(name=name, email = email, phone=phone, location=location, file= file ,subject=subject )
        data.save()
    return render(request, 'joinus.html')

def tray(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'tray.html', {'thank':thank, 'id':id})
    return render(request, 'tray.html')

def about(request):
    return render(request, 'about.html')