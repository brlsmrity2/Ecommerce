from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {"title":"Smrity"}
    return render(request, "home_page.html",context)

def about_page(request):
    return render(request, "about_page.html",{})

def contact_page(request):
    return render(request, "contact_page.html",{})