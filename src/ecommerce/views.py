from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {"title":"Smrity"}
    return render(request, "home_page.html",context)

def about_page(request):
    return render(request, "about_page.html",{})

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':"CONTACT",
        "content":"Welcome to Contact Page",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html",context) 