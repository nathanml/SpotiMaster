from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
]