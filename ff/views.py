from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def landing(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    else:
        return HttpResponse("You need to login!")

def home(request):
    u = Person.objects.get(user=request.user)
    return HttpResponse("Your fics will appear here "+ u.user.email + "!")
