from django.shortcuts import render

def index(request):
    templateData = {}
    templateData["title"] = "Movies Store"
    return render(request, 'home/index.html', {"templateData": templateData})

def about(request):
    templateData = {}
    templateData["title"] = "About"
    return render(request, 'home/about.html', {"templateData": templateData})
