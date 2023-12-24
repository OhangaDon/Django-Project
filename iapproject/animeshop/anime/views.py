from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def anime(request):
    template = loader.get_template('anime.html')
    return HttpResponse(template.render())

def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def Login(request):
    return redirect('anime')