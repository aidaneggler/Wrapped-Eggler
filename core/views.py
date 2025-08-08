import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import time
import pandas as pd
from collections import Counter, defaultdict

# ==============================================================================
# Helper Functions
# These functions help keep the main view logic clean.
# ==============================================================================

def get_spotify_oauth():
    """Helper function to get a SpotifyOAuth instance."""
    return SpotifyOAuth(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
        scope=settings.SPOTIPY_SCOPE
    )

def get_spotify_client(request):
    """
    Helper function to get an authenticated Spotify client.
    It handles token checking, expiration, and refreshing.
    """
    token_info = request.session.get('token_info', None)
    if not token_info:
        return None

    now = int(time.time())
    is_expired = token_info.get('expires_at', 0) < now
    if is_expired:
        sp_oauth = get_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        token_info['expires_at'] = int(time.time()) + token_info['expires_in']
        request.session['token_info'] = token_info

    return spotipy.Spotify(auth=token_info['access_token'])

# ==============================================================================
# Authentication Views
# These views handle the login, logout, and callback flow.
# ==============================================================================

def login(request):
    """Redirects the user to the Spotify authorization page."""
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def logout(request):
    """Logs the user out by clearing the session."""
    if 'token_info' in request.session:
        del request.session['token_info']
    return redirect(reverse('index'))

def callback(request):
    """Handles the callback from Spotify after the user has authenticated."""
    sp_oauth = get_spotify_oauth()
    code = request.GET.get('code')
    token_info = sp_oauth.get_access_token(code)
    token_info['expires_at'] = int(time.time()) + token_info['expires_in']
    request.session['token_info'] = token_info
    return redirect(reverse('dashboard'))

# ==============================================================================
# Page Views
# These views render the actual pages of the application.
# ==============================================================================

def index(request):
    """Renders the home page."""
    return render(request, 'spotify_wrapped_app/index.html')

def dashboard(request):
    """Renders the main dashboard page with links to feature pages."""
    if not request.session.get('token_info'):
        return redirect('login')
    return render(request, 'spotify_wrapped_app/dashboard.html')

def top_artists_view(request):
    """Fetches and displays the user's top 10 artists."""
    sp = get_spotify_client(request)
    if not sp:
        return redirect('login')
    
    top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')
    context = {'top_artists': top_artists['items']}
    return render(request, 'spotify_wrapped_app/top_artists.html', context)

def top_artists_view(request, time_range='medium_term'):
    sp = get_spotify_client(request)
    if not sp:
        return redirect('login')

    valid_time_ranges = ['short_term', 'medium_term', 'long_term']
    if time_range not in valid_time_ranges:
        time_range = 'medium term'

    top_artists = sp.current_user_top_artists(limit=50, time_range=time_range)
    context = {
        'top_artists': top_artists['items'],
        'active_time_range': time_range}
    return render(request, 'spotify_wrapped_app/top_artists.html', context)

def top_tracks_view(request, time_range='medium_term'):
    """Fetches and displays the user's top 10 tracks."""
    sp = get_spotify_client(request)
    if not sp:
        return redirect('login')

    valid_time_ranges = ['short_term', 'medium_term', 'long_term']
    if time_range not in valid_time_ranges:
        time_range = 'medium term'
    
    top_tracks = sp.current_user_top_tracks(limit=50, time_range=time_range)
    context = {
        'top_tracks': top_tracks['items'],
        'active_time_range': time_range}
    return render(request, 'spotify_wrapped_app/top_tracks.html', context)

def top_genres_view(request, time_range='medium_term'):
    sp = get_spotify_client(request)
    if not sp:
        return redirect('login')

    valid_time_ranges = ['short_term', 'medium_term', 'long_term']
    if time_range not in valid_time_ranges:
        time_range = 'medium_term'

    top_artists = sp.current_user_top_artists(limit=50, time_range=time_range)
    genre_counter = Counter()
    for artist in top_artists['items']:
        genre_counter.update(artist.get('genres', []))

    top_genres = genre_counter.most_common(10)
    labels = [genre for genre, _ in top_genres]
    data = [count for _, count in top_genres]

    context = {
        'genre_labels': labels,
        'genre_data': data,
        'active_time_range': time_range
    }
    return render(request, 'spotify_wrapped_app/top_genres.html', context)


