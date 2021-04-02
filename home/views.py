from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    
    return render(request, 'home.html',context)
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message , date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')
    return render(request, 'contact.html')

def page(request):
    return render(request, 'page.html')