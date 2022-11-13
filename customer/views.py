from django.shortcuts import render,redirect
from web.models import *

# Create your views here.
def home(request):
    product=Product.objects.filter(status="On Going")
    context={
        "product":product
    }
    return render(request,'customer/index.html',context)

def viewproduct(request,id):
    productdetails =Product.objects.get(id=id)
    print(request.user)
    if request.method == "POST":
        applyprice=request.POST['applyprice']
        productid=request.POST['productid']
        proid=Product.objects.get(id=productid)
        custid=Customer.objects.get(id=request.user.customer.id)
        print(proid,custid)
        itemsave=BidProduct(customer=custid,product=proid,price=applyprice)
        itemsave.save()
        Product.objects.filter(id=productid).update(price=applyprice)
        return redirect('/customer/')
    context={
        "productdetails":productdetails
    }
    return render(request,'customer/viewproduct.html',context)

def timeout(request,id):
    Product.objects.filter(id=id).update(status="Time Out")
    return redirect('/customer/')