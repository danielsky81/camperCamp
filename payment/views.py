from django.shortcuts import render, redirect, reverse

def payment(request):
    return render(request, 'payment.html')

