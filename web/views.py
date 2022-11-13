from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout,get_user_model
from .models import *
# Create your views here.
def home(request):
    bidlist=BidProduct.objects.all()
    products=Product.objects.all()
    context={
        "bidlist":bidlist,
        "products":products
    }
    return render(request,'web/home.html',context)


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return redirect('web:home')
            elif user.customer != None:
                return redirect('customer:home')
        else:
            msg = "* Incorrect email or password *"
            return render(request,'web/login.html',{'msg':msg,})
    return render(request,'web/login.html')    


def log_out(request):
    logout(request)
    return redirect('/login')


def register(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        reguser = Customer(name=name, phone=phone, email=email, password=password,)
        reguser.save()
        User = get_user_model()
        User.objects.create_user(email=email, password=password,customer=reguser)
        return redirect('/login')
    return render(request,'web/register.html')    

def productlist(request):
    productlist=Product.objects.all()
    context={
    "productlist":productlist
    }
    return render(request,'web/productlist.html',context)     


def addproduct(request):
    if request.method == "POST":
        name=request.POST['name']
        price=request.POST['price']
        duration=request.POST['duration']
        file=request.FILES['file']
        enddate=request.POST['enddate']
        product=Product(name=name, price=price, duration=duration, image=file, endingdate=enddate)
        product.save()
        return redirect('/productlist')

    return render(request,'web/addproduct.html') 


def customerlist(request):
    customerlist=Customer.objects.all()
    context={
    "customerlist":customerlist
    }
    return render(request,'web/customerlist.html',context)
    
def viewhistory(request,id):
    productid=Product.objects.get(id=id)
    viewhistory=BidProduct.objects.filter(product=productid)
    finalresult=BidProduct.objects.filter(product=productid).last()
    print(finalresult,'%'*10)
    context={
    "viewhistory":viewhistory,
    "finalresult":finalresult
    }
    return render(request,'web/viewhistory.html',context)

    