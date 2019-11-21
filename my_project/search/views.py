from django.shortcuts import render
from django.conf import settings 
from .forms import CitySearchForm
import requests

# Create your views here.
def result(request, keyword):
    print('result')
    search_result = {}
    endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&keyword={keyword}'
    url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='20', keyword=keyword)
    response = requests.get(url)
    if response.status_code == 200:
        response_result = response.json
        print(response_result)
        search_result = response_result["_embedded"]['events']
        return render(request, 'search/result.html', {'search_result': search_result})
    else:
        if response.status_code == 404:
            search_message = 'No result found for "%s"' % keyword
        else:
            search_message = "System error. Please try it latter!"
        return render(request, 'search/result.html', {'search_message': search_message})
    
                
    #if 'city' in request.GET:
        #form = CitySearchForm(request.GET)
        #if form.is_valid():
            #search_result = form.search
    #else:
        #form = CitySearchForm()
    #return render(request, 'search/city.html', {'form': form, 'search_result': search_result})


def search(request):
    search_result = {}
    endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&countryCode={countryCode}&classificationName={classificationName}&size={size}'
    url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, countryCode='US', classificationName='music', size='200')
    response = requests.get(url)

    # check whether the call is successful 
    if response.status_code == 200:
        response_result = response.json()
        search_result = response_result["_embedded"]['events']
        return render(request, 'search/result.html', {'search_result': search_result})
    else: 
        search_message = 'There is no result found!'
        return render(request, 'search/result.html', {'search_message': search_message})

    
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



