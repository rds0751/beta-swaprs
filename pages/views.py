from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
    }

    return render(request, 'pages/index.html', context)


def about(request):

    context = {
    }

    return render(request, 'pages/about.html', context)

def start(request):

    context = {
    }

    return render(request, 'pages/start.html', context)

def profile(request):

    context = {
    }

    return render(request, 'pages/profile.html', context)

def settings(request):

    context = {
    }

    return render(request, 'pages/settings.html', context)

def add_wish(request):

    context = {
    }

    return render(request, 'pages/add_wish.html', context)

def edit_item(request):

    context = {
    }

    return render(request, 'pages/edit_item.html', context)

def edit_wish(request):

    context = {
    }

    return render(request, 'pages/edit_wish.html', context)
