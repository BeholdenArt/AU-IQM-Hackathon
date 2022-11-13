from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
    path('business', views.business, name='business'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('health', views.health, name='health'),
    path('science', views.science, name='science'),
    path('sports', views.sports, name='sports'),
    path('technology', views.technology, name='technology'),
    path('profile', views.profile, name='profile'), 
]

