from django.shortcuts import render, redirect, reverse

def dashboard(request):
    return render(request, 'dashboard.html')

