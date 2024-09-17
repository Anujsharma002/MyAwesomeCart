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
    return HttpResponse("i am in contact")
def tracker(reqeust):
    return HttpResponse("i am in tracker")

def search(reqeust):
    return HttpResponse("i am in search")
def productView(reqeust):
    print(Product)
    product = Product.objects.all()
    # pr = Product.objects.get(product_id = Product.product_id)
    return render(reqeust,'shop/prod.html',{'product':product},None)
def checkout(reqeust):
    return HttpResponse("i am in checkout")