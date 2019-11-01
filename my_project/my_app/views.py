import requests
from django.shortcuts import render
from django.http import HttpResponse
from requests.compat import quote_plus

# Create your views here.
def home(request):
    return render(request, 'my_app/home.html')

def login(request):
    return render(request, 'my_app/login.html')

def profile(request):
    return render(request, 'my_app/profile.html')

def search_by_genre(request):
    return render(request, 'my_app/search_by_genre.html')

def search_by_artist(request):
    return render(request, 'my_app/search_by_artist.html')

def search_by_city(request):
    return render(request, 'my_app/search_by_city.html')

