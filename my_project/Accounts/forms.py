from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile

class EditPreferenceForm(UserChangeForm):
    
    class Meta:
        model = UserProfile
        fields = (
            'city',
            'genre',
        )

class EditSpotifyForm(UserChangeForm):   

     class Meta:
        model = UserProfile
        fields = (
            'spotify_username',
        )

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        )
    