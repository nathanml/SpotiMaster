# CS411 Final Project
This project asks us to create a web application, utilizing a database, 
correlating two publicly available data sets, and incorporating third-party authentication.

## Description: SpotiMaster

SpotiMaster is a web app, which attempts to provide the user a list of recommended concerts 
based on their music preference and Spotify listening history. 


## Built With

- [Django](https://www.djangoproject.com/): The web framework used
- [Bootstrap 4](https://getbootstrap.com/): Used to decorate web frontend 
- [TicketMaster API](https://developer.ticketmaster.com/products-and-docs/apis/getting-started/): One of the external API
- [Spotipy](https://spotipy.readthedocs.io/en/latest/): The Python built-in Spotify API
- [allauth](https://django-allauth.readthedocs.io/en/latest/): The django package for OAuth
- [SQLite](https://www.sqlite.org/index.html): The relational database used 

## Installation 

To see how our app works, please download our code and install following packages
```bash
pip install spotipy 
pip install python-decouple
pip install django-naomi
```

## Development

All of codings are inside **my_project** folder.
There are two apps created for this project: accounts and search.

***accounts*** app manages all information and features related to user accounts. The functionality
includes signup, login, view / edit profiles, connect to Spotify, and set up music preferences.

***search*** app deals with all features related to music events. The functionality includes
showing all music events, showing details for one event, searching, and doing recommendation. 

## Documentations 

There are entirely five assignments due for the project: 
- Assignment 1: [Project Pitches](https://github.com/nathanml/CS411-Project/blob/master/Documentations/Assignment%201%20-%20Project%20Pitches.pdf) is under the folder Documentations
- Assignment 2: [User Stories](https://github.com/nathanml/CS411-Project/tree/master/Documentations/Assignment%202%20-%20User%20Stories) is under the folder Documentations
- Assignment 3: [Prototype](https://github.com/nathanml/CS411-Project/tree/master/Documentations/Assignment%203%20-%20Prototype) is under the folder Documentations
- Assignment 4: [Analysis and Architecture Decision](https://github.com/nathanml/CS411-Project/tree/master/Documentations/Assignment%204%20-%20Analysis%20and%20Architecture%20Decision) is under the folder Documentations
- Assignment 5: [OAuth Demo](https://github.com/nathanml/CS411-Project/tree/OAuth) is under the branch OAuth

