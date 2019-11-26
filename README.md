# CS411 Final Project
This project asks us to create a web application, utilizing a database, 
correlating two publicly available data sets, and incorporating third-party authentication.

## Description: SpotiMaster

SpotiMaster is a web app, which attempts to provide the user a list of recommended concerts 
based on their music preference and Spotify listening history. 

Public API: TicketMaster Discovery API, Spotify API
Third-Party Authentication: GitHub, Google

## Installation 

To see how our app works, please download our code and install following packages
```bash
pip install spotipy 
pip install python-decouple
pip install django-naomi
```
spotipy is a Spotify built-in Python package, which helps us call Spotify API.
decouple is a django package, which helps us organize your settings.
naomi is a django package, which helps us set up email backend. 

## Development

All of codings are inside my_project folder.
There are two apps created for this project: accounts and search.

The "accounts" app manages all information and features related to user accounts. The functionality
includes signup, login, view / edit profiles, connect to Spotify, and set up music preferences.

The "search" app deals with all features related to music events. The functionality includes
showing all music events, showing details for one event, searching, and doing recommendation. 

## Documentations 
