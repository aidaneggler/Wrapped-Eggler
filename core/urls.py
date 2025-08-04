from django.urls import path
from . import views

# This is where you define the URL patterns for your app.
# Each path maps a URL to a specific view function from views.py.
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('callback/', views.callback, name='callback'),
    
    # Main dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Feature pages
    path('top-artists/', views.top_artists_view, name='top_artists'),
    path('top-tracks/', views.top_tracks_view, name='top_tracks'),
    path('top-genres/', views.top_genres_view, name='top_genres'),
    path('audio-vibe/', views.audio_vibe_view, name='audio_vibe'),
]
