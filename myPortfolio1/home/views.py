from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=="POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]
        ins = Contact(name=name, phone=phone, email=email, desc=desc)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')