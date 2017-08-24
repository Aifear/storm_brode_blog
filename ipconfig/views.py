from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    ip = request.META['REMOTE_ADDR']
    return HttpResponse('Your ip is: {}'.format(ip))
