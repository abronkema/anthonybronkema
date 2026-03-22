"""
Root URL configuration for config project.

This is the main URL routing file that includes URL patterns from all apps.

Learning concepts:
- include(): Include URL patterns from other apps
- URL namespacing: Each app has its own urls.py for organization
- URL order: Django tries patterns in order, first match wins

URL structure:
- /admin/          → Django admin interface
- /                → Portfolio homepage (from portfolio.urls)

Adding new apps:
When you add a new app (blog, projects, etc.), include its URLs here:
    path('blog/', include('blog.urls')),
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # Portfolio app URLs
    # '' means root URL, so portfolio.urls patterns start at /
    # include() delegates URL handling to the portfolio app's urls.py
    path('', include('portfolio.urls')),
]
