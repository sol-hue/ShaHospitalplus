from django.shortcuts import render

# Create your views here.
def about(request):
    return render('about.html')

def agents(request):
    return render('agents.html')

def contact(request):
    return render('contact.html')

def index(request):
    return render('index.html')

def properties(request):
    return render('properties.html')

def property(request):
    return render('property-single.html')

def service(request):
    return render('service-details.html')

def services(request):
    return render('services.html')

def starter(request):
    return render('starter-page.html')