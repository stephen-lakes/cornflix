from django.shortcuts import render

import requests
import json
from decouple import config
from .forms import SearchForm



def index(request):

    BASE_URL = config('BASE_URL')
    API_KEY = config('API_KEY')
    IMG_BASE_URL = config('IMG_BASE_URL')

    if request.method == 'POST':
        
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            search_term = request.POST.get("search_term")

        resp = requests.get(BASE_URL + '/search/movie?api_key=' + API_KEY + '&language=en-US&query=' + search_term + '&page=1&include_adult=false')
        context = {
            "search_term": search_term,
            "search_results": resp.json()["results"],
            "img_base_url": IMG_BASE_URL,
            "search_results_length": len(resp.json()["results"]),
            "form": form
        }
            
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

        discover = requests.get(BASE_URL + '/discover/movie?sort_by=popularity.desc&api_key=' + API_KEY).json()["results"]
        upcoming = requests.get(BASE_URL + '/movie/upcoming?api_key=' + API_KEY + '&language=en-US&page=1').json()["results"]
        top_rated = requests.get(BASE_URL + '/movie/top_rated?api_key=' + API_KEY + '&language=en-US&page=1').json()["results"]

        context = {
            "discover": discover,
            "upcoming": upcoming,
            "toprated": top_rated,
            "img_base_url": IMG_BASE_URL,
            "form": form
        }
        
    return render(request, 'home.html', context=context)    











'''
Upcoming movies in theater
https://api.themoviedb.org/3/movie/upcoming?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US&page=1


Latest movies
https://api.themoviedb.org/3/movie/latest?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US


Search movies
https://api.themoviedb.org/3/search/movie?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US&query=the%20simpsons&page=1&include_adult=false

Search movies by Keyword
https://api.themoviedb.org/3/search/keyword?api_key=c59e25e2fa584e942f512871beda2fae&query=dance&page=1

Top Rated movies
https://api.themoviedb.org/3/movie/top_rated?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US&page=1

Get Genre List
https://api.themoviedb.org/3/genre/movie/list?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US

Multi Search: movies, tvs, people, etc
https://api.themoviedb.org/3/search/multi?api_key=c59e25e2fa584e942f512871beda2fae&language=en-US&query=will%20smith&page=1&include_adult=false
'''


