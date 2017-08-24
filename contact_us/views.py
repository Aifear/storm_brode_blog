from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError, mail_managers
from .models import ContactForm
from django.template.context_processors import csrf
import smtplib
from .models import Contacts
from django.contrib import auth
# Create your views he

"""def contactView(request):
    args ={}
    args.update(csrf(request))
    if request.POST:
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        from_email = request.POST.get('email','')
        if subject and message and from_email:
            try:
                send_mail(subject,
                          message,
                          'admin@stormbrode.pythonanywhere.com',
                          ['admin@stormbrode.pythonanywhere.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')

        else:
            return HttpResponse('Make shure')
    else:
        return render(request, 'contact_us/index.html', args)"""

def contactView(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        sub = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')
        name = auth.get_user(request)
        if sub and message and from_email:
            add_to_contact(message, sub, from_email, name)
            return redirect ('/')
        else:
            return HttpResponse('MakeSure')
    else:
        return render(request, 'contact_us/index.html', args)




def add_to_contact(message, sub, sender, name):
    contact = Contacts(message=message, sub=sub,sender=sender, name=name)
    contact.save()
    return 'Ok'


def messages(request):
    contacts = Contacts.objects.all()
    if auth.get_user(request).is_staff:
        return render(request, 'contact_us/contacts.html', {'Contacts':contacts})
    else:
        return redirect('/')