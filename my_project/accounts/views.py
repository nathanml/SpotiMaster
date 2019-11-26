import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from requests.compat import quote_plus
from accounts.forms import EditProfileForm, EditPreferenceForm, EditSpotifyForm
from accounts.models import UserProfile

# Create your views here.
def home(request):
    return render(request, 'account/home.html')

def spotify(request):
    return render(request, 'account/spotify.html')

@login_required 
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    genre = ''
    # check genre and get the genre name 
    genre_id = profile.genre
    if genre_id == 'KnvZfZ7vAvd':
        genre = 'Blues'
    elif genre_id == 'KnvZfZ7vAeJ':
        genre = 'Classical'
    elif genre_id == 'KnvZfZ7vAv6':
        genre = 'Country'
    elif genre_id == 'KnvZfZ7vAv1':
        genre = 'Hip-Hop / Rap'
    elif genre_id == 'KnvZfZ7vAvE':
        genre = 'Jazz'
    elif genre_id == 'KnvZfZ7vAev':
        genre = 'Pop'
    elif genre_id == 'KnvZfZ7vAee':
        genre = 'R&B'
    elif genre_id == 'KnvZfZ7vAeA':
        genre = 'Rock'

    args = {
        'user': request.user,
        'profile': profile,
        'genre': genre
    }
    return render(request, 'account/profile.html', args)

@login_required 
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance=request.user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('/accounts/profile/')
            
    else:
        profile_form = EditProfileForm(instance=request.user)
        args = {'profile_form': profile_form,}

        return render(request, 'account/edit_profile.html', args)

@login_required 
def edit_preference(request):
    if request.method == 'POST':
        preference_form = EditPreferenceForm(request.POST, instance=request.user)

        if preference_form.is_valid():
            preference = UserProfile.objects.get(user=request.user)
            preference.city = preference_form.cleaned_data['city']
            preference.genre = preference_form.cleaned_data['genre']
            preference.save()
            return redirect('/accounts/profile/')
            
    else:
        preference_form = EditPreferenceForm(instance=request.user)
        args = {'preference_form': preference_form}

        return render(request, 'account/edit_preference.html', args)

@login_required 
def connect_spotify(request):
    if request.method == 'POST':
        spotify_form = EditSpotifyForm(request.POST, instance=request.user)

        if spotify_form.is_valid():
            preference = UserProfile.objects.get(user=request.user)
            preference.spotify_username = spotify_form.cleaned_data['spotify_username']
            preference.save()
            return redirect('/accounts/profile/')
            
    else:
        spotify_form = EditSpotifyForm(instance=request.user)
        args = {'spotify_form': spotify_form}

        return render(request, 'account/connect_spotify.html', args)


@login_required 
def reset_password(request):
    args = {'user': request.user}
    return render(request, 'account/password_change.html', args)


