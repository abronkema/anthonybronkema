"""
Portfolio App URL Configuration

This file defines the URL patterns for the portfolio app.

Learning concepts:
- URL patterns: Map URL paths to view functions
- path(): Define a URL pattern with a path string and a view
- app_name: Namespace for URL reversing (e.g., {% url 'portfolio:index' %})
- urlpatterns: List of URL patterns Django will try to match in order

URL reversing:
Instead of hardcoding URLs in templates or code, use the URL name:
- In templates: {% url 'portfolio:index' %}
- In views: reverse('portfolio:index')
This way, if you change the URL path, you only update it in one place.
"""

from django.urls import path
from . import views

# App namespace for URL reversing
# Allows you to use 'portfolio:index' to refer to this app's URLs
app_name = 'portfolio'

# URL patterns for this app
urlpatterns = [
    # Homepage: '' means root URL of this app (/)
    # name='index' allows URL reversing: {% url 'portfolio:index' %}
    path('', views.index, name='index'),
]
