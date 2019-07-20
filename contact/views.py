from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages

def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message + ' | Email sent from: ' + your_email, your_email, ['djangoprojectci@gmail.com'])
                messages.success(request, 'Thank you for your message!')
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
            return redirect(reverse('hello'))   
        else:
            messages.error(request, 'There was a problem with the contact form. Please try again later.')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})


