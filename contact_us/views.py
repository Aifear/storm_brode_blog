from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError, mail_managers
from .models import ContactForm
from django.template.context_processors import csrf
import smtplib
# Create your views he

def contactView(request):
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
                          from_email,
                          ['kimolav@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')

        else:
            return HttpResponse('Make shure')
    else:
        return render(request, 'contact_us/index.html', args)

