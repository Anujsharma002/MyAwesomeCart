from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Product,Contact,Order,Orderupdate
from math import ceil
import json
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
    if reqeust.method == "POST":
        orderId = reqeust.POST.get('orderId', '')
        email = reqeust.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = Orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].text_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

        return render(reqeust, 'shop/tracker.html')
    return render(reqeust, 'shop/tracker.html')

def search(reqeust):
    return render(reqeust, 'shop/search.html')
def productView(reqeust,myid):
    print(Product)
    prod = Product.objects.filter(id=myid)
    # pr = Product.objects.get(product_id = Product.product_id)
    return render(reqeust,'shop/prod.html',{'product':prod[0]})
def checkout(reqeust):
    thank = False
    id = 0
    if reqeust.method == "POST":
     text_json = reqeust.POST.get('itemsJson','')
     name = reqeust.POST.get('name', '')
     email = reqeust.POST.get('email', '')
     add1 =  reqeust.POST.get('address1', '') + ' ' + reqeust.POST.get('address2', '')
     city = reqeust.POST.get('city', '')
     state = reqeust.POST.get('state', '')
     phone = reqeust.POST.get('phone', '')
     zip_code = reqeust.POST.get('zip', '')
     print(text_json)
     order = Order(name=name, email=email, phone=phone, text_json = text_json,address =add1,city= city,state=state,zip_code=zip_code)
     order.save()
     update = Orderupdate(order_id=order.order_id, update_desc="The order has been placed")
     update.save()
     thank = True
     id = order.order_id
     return render(reqeust, 'shop/checkout.html',{"thank": thank,"id": id})
    return render(reqeust, 'shop/checkout.html')