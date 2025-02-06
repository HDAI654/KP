from django.shortcuts import render
from django.http import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import forms

# Create your views here.

def login_page(request):
    form = forms.flogin()
    return render(request=request, template_name="login.html", context={"form":form})

def check_login(request):
    form = forms.flogin(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            res = HttpResponseRedirect("/panel")
            res.set_cookie('username', str(username))
            return res
        else:
            return HttpResponseRedirect("login")
    else:
        return HttpResponseRedirect("login")
    