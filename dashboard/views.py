from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def dashboard(request):
    return render(request, 'dashboard.html')

