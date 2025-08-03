import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import time

def get_spotify_oauth():
    """
    Helper function to get a SpotifyOAuth instance.
    """
    return SpotifyOAuth(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
        scope=settings.SPOTIPY_SCOPE
    )

def login(request):
    """
    Redirects the user to the Spotify authorization page.
    """
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def logout(request):
    """
    Logs the user out by clearing the session.
    """
    if 'token_info' in request.session:
        del request.session['token_info']
    return redirect(reverse('index'))


def callback(request):
    """
    Handles the callback from Spotify after the user has authenticated.
    The authorization code is exchanged for an access token.
    """
    sp_oauth = get_spotify_oauth()
    # The user is redirected back with a 'code' query parameter
    code = request.GET.get('code')
    
    # Exchange the code for an access token
    token_info = sp_oauth.get_access_token(code)

    # Save the token info in the session.
    # We also add an 'expires_at' timestamp to manage token expiration.
    token_info['expires_at'] = int(time.time()) + token_info['expires_in']
    request.session['token_info'] = token_info

    return redirect(reverse('results'))

def index(request):
    """
    Renders the home page. If the user is already logged in,
    it will show a link to the results and a logout button.
    """
    return render(request, 'spotify_wrapped_app/index.html')

def results(request):
    """
    Fetches and displays the user's Spotify data.
    """
    token_info = request.session.get('token_info', None)

    # If no token, redirect to login
    if not token_info:
        return redirect(reverse('login'))

    # Check if token is expired
    now = int(time.time())
    is_expired = token_info.get('expires_at', 0) < now

    if is_expired:
        sp_oauth = get_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        token_info['expires_at'] = int(time.time()) + token_info['expires_in']
        request.session['token_info'] = token_info

    try:
        # Create a Spotify client with the access token
        sp = spotipy.Spotify(auth=token_info['access_token'])

        # Fetch user's top artists and tracks
        top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')
        top_tracks = sp.current_user_top_tracks(limit=10, time_range='medium_term')
        
        context = {
            'top_artists': top_artists['items'],
            'top_tracks': top_tracks['items'],
        }
        return render(request, 'spotify_wrapped_app/results.html', context)

    except spotipy.SpotifyException as e:
        # Handle potential errors, e.g., token revoked
        return redirect(reverse('logout'))
