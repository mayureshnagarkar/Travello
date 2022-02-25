from django.shortcuts import render
from datetime import datetime
from way.models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, phone=phone, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')