from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie

# Create your views here.



def index(request):
    films = Movie.objects.order_by('title')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'films': films}, request))

def movies(request, movie_id):
    movie = movie.objects.get(pk = movie_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))