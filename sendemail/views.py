from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailsend(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
        try:
            send_mail(subject, message, from_email,
                      ['photography.philosophy.lc.com@gmail.com'])
            messages.success(request, 'Success! Thank you for your message.')
        except BadHeaderError:
            messages.error(request, 'Invalid header found.')
    return redirect('contact')


def success(request):

    template = 'home/contact.html'
    return render(request, template)
