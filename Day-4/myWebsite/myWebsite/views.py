from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
def home(request: HttpRequest) -> HttpResponse:
    return render(request,'index.html')
def about(request: HttpRequest) -> HttpResponse:    
    return HttpResponse("This is the about page.")  
def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is the contact page.")
def services(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is the services page.")
 