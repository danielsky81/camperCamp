from django.shortcuts import render, redirect, reverse

def contact(request):
    return render(request, 'contact.html')