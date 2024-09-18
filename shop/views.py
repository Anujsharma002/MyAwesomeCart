from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
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