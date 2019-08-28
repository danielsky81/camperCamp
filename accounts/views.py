from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'You have successfully logged in! Enjoy!')
                return redirect(reverse('dashboard'))
            else:
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
            username = request.POST['username']
            password = request.POST['password1']
            user = User.objects.get(username=username)
            profile = Profile(
                user=user,
                first_name=request.POST['first_name'],
                surname=request.POST['last_name'],
                email=request.POST['email'],
                username=request.POST['username']
            )
            profile.save()
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, 'Unable to register your account at this time')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {'registration_form': registration_form})


def update_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                profile.updated_date = timezone.now()
                profile = form.save()
                return redirect('dashboard')
        else:
            form = ProfileForm(instance=profile)
    return render(request, 'profileform.html', {
        'form': form,
        'profile': profile
    })


def delete_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user.is_authenticated:
        user.delete()
        messages.success(request, 'Your Profile has been removed from our application')
    return redirect('hello')
