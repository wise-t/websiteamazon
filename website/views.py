from django.shortcuts import render

def home(request):
    return render (request,'pages/home.html') 

def about(request):
    return render (request,'pages/about.html')

def news(request):
    return render (request,'pages/news.html') 
    
def article1(request):
    return render (request,'pages/article1.html')  

def contact(request):
    return render (request,'pages/contact.html')


def elements(request):
    return render (request,'pages/elements.html')

def destinations(request):
    return render (request,'pages/destinations.html')


def index (request):
    return render (request,'pages/index.html')


def settings(request):
    return render (request,'pages/settings.html') 

def handler404(request,exception=None):
    return render (request,'errors/404.html', {'error':exception},status=404) 

def handler500(request,exception =None):
    return render (request,'errors/500.html', {},status=500)  