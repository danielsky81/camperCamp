from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
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
                # login_form.add_error(None, 'Your username or password is incorrect. Please try again.')
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
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username=request.POST['username']
            password=request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, 'Unable to register your account at this time')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        'registration_form': registration_form})