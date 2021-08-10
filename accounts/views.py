import products
import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from api.models import *
from api.serializers import ProductSerializer

from products.models import category


from .models import *
# from products.models.product import Product
# from products.models.category import Category
# Create your views here.


def home(request):
    return render(request, 'index.html')

def prof(request):
    return render(request, '404.html')

def blog(request):
    return render(request, 'blog.html')

def blogs(request):
    return render(request, 'blog-single.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')


def update_profile(request):
    data = profile.objects.get(user__id=request.user.id)
    context={'data':data}
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        ph=request.POST["ph"]
        pin=request.POST["pin"]
        state=request.POST["state"]
        address=request.POST["address"]
        town=request.POST["town"]
        city=request.POST["city"]
        
        

        Usr = User.objects.get(id=request.user.id)
        Usr.first_name = name
        Usr.email = email
        Usr.save()

        
        data.name = name
        
        data.phone = ph
        data.email = email
        data.pin_code = pin
        data.address = address
        data.state = state
        data.city = city
        


        data.save()
    

    return render(request, 'profile.html',context)

def contact(request):
    return render(request, 'contact-us.html')

def All_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True )
    # obj = Product.objects.get(id=1)
    # context = {
        
    #     'Name':products.Name,
    #     'cat':products.category,
    #     'desc':products.description,
    #     'image':products.Image
    # }
    context =  {'products': products, 'serializer': serializer}
    return render(request, 'shop.html', context)


def product(request):
    return render(request, 'product-details.html')

def shop(request):
    product = products.get_all_products()
    context = {'Products':product}
    return render(request, 'shop.html', context)


def home(request):
    return render(request, 'index.html')

def manageadd(request):
    return render(request, 'manageadd.html')


def m(request):
    return render(request, 'm.html')

def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:

            messages.warning(request, 'Please enter valid credentials or register first !!!')
            return redirect('handlelogin')
            
    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    return redirect('home')
    return HttpResponse('handleLogout')


def handlesignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        username = request.POST['phn']
        pass1 = request.POST['pass1']
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exist")
        else: 
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.save()

            ak = profile(user=myuser, name=fname, email=email, phone=username)
            ak.save()
            return redirect('home')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')
        

