from django.shortcuts import render
from .models import Movie

def index(request):
    templateData = {}
    templateData['title'] = 'Movies'
    templateData['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html', {'templateData': templateData})

def show(request, id):
    templateData = {}
    movie = Movie.objects.get(id=id)
    templateData['title'] = movie.name
    templateData['movie'] = movie
    return render(request, 'movies/show.html', {'templateData': templateData})