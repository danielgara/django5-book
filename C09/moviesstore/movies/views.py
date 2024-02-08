from django.shortcuts import render, redirect
from .models import Movie, Review
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request):
    templateData = {}
    templateData['title'] = 'Movies'
    templateData['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html', {'templateData': templateData})

def show(request, id):
    templateData = {}
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    templateData['title'] = movie.name
    templateData['movie'] = movie
    templateData['reviews'] = reviews
    return render(request, 'movies/show.html', {'templateData': templateData})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('movies.show', id=id)
