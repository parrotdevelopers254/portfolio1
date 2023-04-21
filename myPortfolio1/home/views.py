from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my Homepage")

def contact(request):
    return HttpResponse("This is the contact page.")

def about(request):
    return HttpResponse("This is the about page.")

def projects(request):
    return HttpResponse("This is the projects page.")