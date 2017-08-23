from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csfr

def login(request):
    args={}
    args.update(csfr(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate (username=username, password=password)
        if user is not None:
            auth.Login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'User is not defined'
            return render(request, 'login/login.html', args)

    else:
        return render(request, 'login/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
