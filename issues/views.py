from django.shortcuts import render, redirect, reverse

def issues(request):
    return render(request, 'issues.html')