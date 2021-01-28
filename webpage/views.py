from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name').title()
            email = request.POST.get('email').lower()
            text_message = request.POST.get('message').capitalize()
            Contact.objects.create(name=name, email=email, message=text_message)
            email_message_contact(name, email, text_message)

            return redirect('contact')
    else:
        form = ContactForm()
        return render(request, 'webpage/contact.html', {'form': form})


def email_message_contact(name, email, text_message):
    email_subject = 'Personal WebPage Contact Notification'
    text_message = f'Hola Matias, una persona llamada, {name}, y con Email {email}, te ha enviado el siguiente mensaje \n\n' \
                   f'{text_message} '
    to_email = 'matiascocciolo@gmail.com'
    email = EmailMessage(email_subject, text_message, to=[to_email])
    email.send()


    return
