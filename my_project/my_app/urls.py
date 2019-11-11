from django.urls import path

from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='my_app/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('search/genre/', views.search_by_genre, name='search_by_genre'),
    path('search/artist/', views.search_by_artist, name='search_by_artist'),
    path('search/city/', views.search_by_city, name='search_by_city'),
    path('login/', LoginView.as_view(template_name="login.html"), name = 'login')

]