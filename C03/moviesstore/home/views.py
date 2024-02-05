from django.shortcuts import render

def index(request):
    viewData = {}
    viewData["title"] = "Movies Store"
    return render(request, 'home/index.html', {"viewData": viewData})

def about(request):
    viewData = {}
    viewData["title"] = "About"
    return render(request, 'home/about.html', {"viewData": viewData})
