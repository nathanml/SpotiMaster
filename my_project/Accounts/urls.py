from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/edit', views.edit_profile, name='edit_profile'),
    path('accounts/preference/edit', views.edit_preference, name='edit_preference'),
    path('accounts/spotify/connect', views.connect_spotify, name='connect_spotify'),
    path('accounts/password/', views.reset_password, name='reset_password')
]