from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully logged in! Enjoy!')
                return redirect(reverse('dashboard'))
            else:
                # login_form.add_error(None, "Your username or password is incorrect. Please try again.")
                messages.error(request, 'Your username or password is incorrect. Please try again.')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out. See you soon!')
    return redirect(reverse('hello'))

def registration(request):
    return render(request, 'registration.html')