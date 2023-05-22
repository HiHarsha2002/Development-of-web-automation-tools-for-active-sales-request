from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')    

def scope(request):
    return render(request,'scope.html' )

def product(request):
    return render(request,'product.html' )

def scrapdata(request):
    return render(request,'scrapdata.html' )