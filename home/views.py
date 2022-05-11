from django.http import HttpResponse
from django.shortcuts import render, redirect
from pluggy import PluginManager

from .models import PG
# Create your views here.
def home(request):
    return render(request, "home/home.html")


def sell(request):
    return render(request, "home/addpg.html")



def contact(request):
    return render(request, "home/contact.html")
def about(request):
    return render(request, "home/aboutus.html")
     
     
def rent(request):
    
        
    
    
        return render(request, "home/rent.html", )
    
     
     
def addpg(request):
    if request.method == "POST":
        Pgname=request.POST.get("Pgname")
        Contact=request.POST.get("Contact")
        Rent=request.POST.get("Rent")
        Address=request.POST.get("Address")
        City=request.POST.get("City")
        State=request.POST.get("State")
        ZipPg=request.POST.get("Zip")
        Image=request.POST.get("PgImage")
        pg = PG(name=Pgname, contact= Contact, rent= Rent, address=Address, city=City,state=State, zipcode=ZipPg, image=Image)
        pg.save()
        
        
        
        return redirect("/")
            
    return redirect("/")
                 
                 