from django.shortcuts import render
from .models import Movie

def index(request):
    viewData = {}
    viewData['title'] = 'Movies'
    viewData['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html', {'viewData': viewData})

def show(request, id):
    viewData = {}
    movie = Movie.objects.get(id=id)
    viewData['title'] = movie.name
    viewData['movie'] = movie
    return render(request, 'movies/show.html', {'viewData': viewData})