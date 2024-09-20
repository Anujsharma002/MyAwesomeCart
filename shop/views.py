from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.
def index(request):
    # print(Product)
    product = Product.objects.all()

    allProd = []
    catProds = Product.objects.values('category','id')
    cats= {item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        len_product = n // 4 + ceil((n / 4) - (n // 4))
        rangen = range(1, len_product)
        allProd.append([prod,rangen,len_product])
    params = {'allProd':allProd}
    # print(rangen)
    # allProd = [[product,rangen,len_product],[product,rangen,len_product]]
    # # params = {'product':product,'n':len_product,'range':rangen,'nslides':len_product}
    # params ={'allProd':allProd}
    # print(params)
    return render(request,'shop/index.html',params)
def about(reqeust):
    return render(reqeust,'shop/about.html')
def contact(reqeust):
    if reqeust.method == "POST":
        # print(reqeust)
        name = reqeust.POST.get('name','')
        email = reqeust.POST.get('email','')
        phone = reqeust.POST.get('phone','')
        message= reqeust.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        send_mail(f"message from name:{name} user:{email}", message,settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    return render(reqeust, 'shop/contact.html')
def tracker(reqeust):
    return render(reqeust, 'shop/tracker.html')

def search(reqeust):
    return render(reqeust, 'shop/search.html')
def productView(reqeust,myid):
    print(Product)
    prod = Product.objects.filter(id=myid)
    # pr = Product.objects.get(product_id = Product.product_id)
    return render(reqeust,'shop/prod.html',{'product':prod[0]})
def checkout(reqeust):
    return render(reqeust, 'shop/checkout.html')