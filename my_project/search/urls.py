from django.urls import path

from . import views

urlpatterns = [
    path('result/', views.result, name='result'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('', views.search, name='search'),
    path('<str:event_id>/', views.event_detail, name='detail'),
]