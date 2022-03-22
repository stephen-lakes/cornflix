from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
import requests
import json
from decouple import config



def index(request):
    resp = requests.get(config('BASE_URL') + '/discover/movie?sort_by=popularity.desc&api_key=' + config('API_KEY'))
    context = {"movies": resp.json()["results"],
    "img_base_url": config('IMG_BASE_URL')
    }
    
    return render(request, 'home.html', context=context)    
