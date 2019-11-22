import requests
from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from accounts.models import UserProfile

# set up for Spotipy Library 
import spotipy
import spotipy.util as util


# Create your views here.

# get the recommendation for a user
def recommendation(request):
    profile = UserProfile.objects.get(user=request.user)
    username = profile.spotify_username
    city = profile.city
    genre = profile.genre
    search_result = []

    if city == '' and genre == '' and username == '':
        search_message = "There is no recommendation for you. Please either set up your preference or connect to your Spotify account first!"
        return render(request, 'search/result.html', {'search_message': search_message})
    
    else:
        # check whether username is an empty string 
        if username != '':
            artists = []
            scope = 'user-top-read'
            client_id = settings.SPOTIFY_API_KEY
            client_secret = settings.SPOTIFY_API_SECRET
            redirect_uri = 'http://127.0.0.1:8000/spotifylogin'

            token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
            
            if token:
                sp = spotipy.Spotify(auth=token)
                sp.trace = False
                results = sp.current_user_top_artists(time_range='long_term', limit=20)
                for item in results['items']:
                    artists.append(item['name'])
            
            # call Ticketmaster API
            for artist in artists:
                endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&keyword={keyword}'
                url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='4', keyword=artist)
                response = requests.get(url)
                if response.status_code == 200:
                    response_result = response.json()
                    total_element = response_result['page']['totalElements']
                
                    if total_element != 0:
                        events = response_result["_embedded"]['events']
                        for event in events:
                            search_result.append(event)
            #return render(request, 'search/result.html', {'search_result': search_result})
        
        if city != '' or genre != '':
            url = ''
            if city == '':
                endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&genreId={genreId}'
                url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='100', genreId=genre)
            elif genre == '':
                endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&city={city}'
                url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='100', city=city)
            else:
                endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&city={city}&genreId={genreId}'
                url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='100', city=city, genreId=genre)
            response = requests.get(url)
            if response.status_code == 200:
                response_result = response.json()
                total_element = response_result['page']['totalElements']
                if total_element != 0:
                    events = response_result["_embedded"]['events']
                    for event in events:
                        search_result.append(event)
                else:
                    search_message = "Sorry, there is no recommendation for you based on your preference right now!"
                    return render(request, 'search/result.html', {'search_message': search_message})

        return render(request, 'search/result.html', {'search_result': search_result})

    


# get the searching result
def result(request):
    search_result = {}
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&keyword={keyword}&classificationName={classificationName}&size={size}'
        url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, keyword=keyword, classificationName='music', size='50',)
        response = requests.get(url)
        if response.status_code == 200:
            response_result = response.json()
            total_element = response_result['page']['totalElements']
            if total_element != 0:
                search_result = response_result["_embedded"]['events']
                return render(request, 'search/result.html', {'search_result': search_result})
            else:
                search_message = 'No result found for "%s"' % keyword
                return render(request, 'search/result.html', {'search_message': search_message})
        else:
            if response.status_code == 404:
                search_message = 'No result found for "%s"' % keyword
            else:
                search_message = "System error. Please try it latter!"
            return render(request, 'search/result.html', {'search_message': search_message})
    
# get all of music events
def search(request):
    search_result = {}
    endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&countryCode={countryCode}&classificationName={classificationName}&size={size}'
    url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, countryCode='US', classificationName='music', size='200')
    response = requests.get(url)

    # check whether the call is successful 
    if response.status_code == 200:
        response_result = response.json()
        total_element = response_result['page']['totalElements']
        if total_element != 0:
            search_result = response_result["_embedded"]['events']
            return render(request, 'search/result.html', {'search_result': search_result})
    else: 
        search_message = 'There is no result found!'
        return render(request, 'search/result.html', {'search_message': search_message})

# display the detail of a music event   
def event_detail(request, event_id):
    search_result = {}
    endpoint = 'https://app.ticketmaster.com/discovery/v2/events/{id}?apikey={apikey}'
    url = endpoint.format(id=event_id, apikey=settings.TICKETMASTER_API_KEY)
    response = requests.get(url)
    # check whether the call is successful 
    if response.status_code == 200:
        response_result = response.json()
        search_result['name'] = response_result['name']
        search_result['url'] = response_result['url']
        search_result['images'] = response_result['images'][0]
        search_result['dates'] = response_result['dates']['start']
        search_result['genre'] = response_result['classifications'][0]['genre']['name']
        search_result['venue'] = response_result['_embedded']['venues'][0]
        return render(request, 'search/detail.html', {'search_result': search_result})
    else:
        search_message = 'There is no result found!'
        return render(request, 'search/result.html', {'search_message': search_message})



