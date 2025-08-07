from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('callback/', views.callback, name='callback'),
    
    # Main dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Feature pages
    path('top-artists/', views.top_artists_view, name='top_artists'),
    path('top-genres/', views.top_genres_view, name='top_genres'),

    # This single URL pattern now handles all requests for top tracks
    path('top-artists/<str:time_range>/', views.top_artists_view, name='top_artists'),
    path('top-tracks/<str:time_range>/', views.top_tracks_view, name='top_tracks'),
    path('top-genres/<str:time_range>/', views.top_genres_view, name='top_genres'),
]

