"""
Development settings for local development.

These settings are optimized for development work:
- DEBUG mode enabled for detailed error pages
- Permissive ALLOWED_HOSTS for localhost
- SQLite database for simplicity
- Django serves static files automatically

To use these settings, set the environment variable:
    export DJANGO_SETTINGS_MODULE=config.settings.development

Or add it to your .env file.
"""

from .base import *

# Debug mode shows detailed error pages
# NEVER set this to True in production!
DEBUG = True

# Allow localhost and 127.0.0.1 for local development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# SQLite database for development
# Simple, file-based database - no server needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
