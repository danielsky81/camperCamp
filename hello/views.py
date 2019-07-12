from django.shortcuts import render, HttpResponse

def welcome(request):
    return HttpResponse("Hello World!")
