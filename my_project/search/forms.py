from django import forms
from django.conf import settings
import requests

class CitySearchForm(forms.Form):
    city = forms.CharField(max_length=100)

    def search(self):
        result = {}
        city = self.cleaned_data['city']
        endpoint = 'https://app.ticketmaster.com/discovery/v2/events?apikey={apikey}&classificationName={classificationName}&size={size}&city={city}'
        url = endpoint.format(apikey=settings.TICKETMASTER_API_KEY, classificationName='music', size='20', city=city)
        response = requests.get(url)
        if response.status_code == 200:
            response_result = response.json
            result = response_result["_embedded"]['events']
            result['sucess'] = True
        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No result found for "%s"' % city
            else:
                result['message'] = "System error. Please try it latter!"
        return result 