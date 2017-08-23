from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print (username, password)
        user = auth.authenticate (username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'User is not defined'
            return render(request, 'login/login.html', args)

    else:
        return render(request, 'login/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
