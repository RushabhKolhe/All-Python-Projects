from django.shortcuts import render
from django.http.response import HttpResponse
from . models import Product,Email,Checkout
import math
# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    #n=len(products)
    #nslides = n // 4 + ceil((n / 4) - (n // 4))
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + math.ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])
    #params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    # allprods=[[products,range(1,nslides),nslides],
    #           [products,range(1,nslides),nslides]]
    params={'allprods':allprods}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        message=request.POST.get('message','')
        print(name,email,message)
        contacts=Email(name=name,email=email,message=message)
        contacts.save()
    #return HttpResponse("contact")
    return render(request,"shop/contact.html")
def tracker(request):
    #return HttpResponse("tracker")
     return render(request,"shop/tracker.html")
def search(request):
    return HttpResponse("search")

def productview(request, myid):
    #fetch the product using id
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html", {'product':product[0]})
def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone=request.POST.get('phone', '')
        print(name, email, address,address2,city,state,zip,phone)
        order = Checkout(name=name, email=email, address=address, address2=address2, city=city,state=state,zip=zip,phone=phone)
        order.save()
   # return HttpResponse("checkout")
    return render(request,'shop/checkout.html')

def submitalert(request):
    return render(request,'shop/submitalert.html')