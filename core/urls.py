from django.urls import path
from . import views

# This is where you define the URL patterns for your app.
# Each path maps a URL to a specific view function from views.py.
urlpatterns = [
    # e.g., http://127.0.0.1:8000/
    path('', views.index, name='index'),
    
    # e.g., http://127.0.0.1:8000/login/
    path('login/', views.login, name='login'),
    
    # e.g., http://127.0.0.1:8000/logout/
    path('logout/', views.logout, name='logout'),
    
    # e.g., http://127.0.0.1:8000/callback/
    path('callback/', views.callback, name='callback'),
    
    # e.g., http://127.0.0.1:8000/results/
    path('results/', views.results, name='results'),
]
