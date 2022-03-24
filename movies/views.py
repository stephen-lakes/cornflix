from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
import requests
import json
from decouple import config



def index(request):
    BASE_URL = config('BASE_URL')
    API_KEY = config('API_KEY')
    IMG_BASE_URL = config('IMG_BASE_URL')

    resp = requests.get(BASE_URL + '/discover/movie?sort_by=popularity.desc&api_key=' + API_KEY)
    context = {
        "movies": resp.json()["results"],
        "img_base_url": IMG_BASE_URL
    }
    
    return render(request, 'home.html', context=context)    
