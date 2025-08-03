from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported

# This is the main URL router for your entire project.
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This line tells Django to hand off any incoming URL requests
    # to the 'urls.py' file inside your 'core' app for further processing.
    path('', include('core.urls')), 
]
