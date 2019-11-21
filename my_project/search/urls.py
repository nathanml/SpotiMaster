from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('result/?keyword=<str:keyword>/', views.result, name='result'),
    path('<str:event_id>/', views.event_detail, name='detail'),
]