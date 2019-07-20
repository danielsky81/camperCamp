from django.shortcuts import render, redirect, reverse

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect(reverse('hello'))

