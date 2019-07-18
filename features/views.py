from django.shortcuts import render, redirect, reverse

def features(request):
    return render(request, 'features.html')