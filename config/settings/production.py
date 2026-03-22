"""
Production settings for Railway deployment.

These settings are optimized for production:
- DEBUG disabled for security
- Restrictive ALLOWED_HOSTS
- SECRET_KEY from environment variable
- WhiteNoise for efficient static file serving
- Security settings enabled (HTTPS, secure cookies)

Environment variables required:
- SECRET_KEY: A long, random string for cryptographic signing
- DJANGO_SETTINGS_MODULE: Should be set to 'config.settings.production'

Learning concepts:
- python-decouple: Manages environment variables
- WhiteNoise: Serves static files efficiently in production
- Security headers: HTTPS redirect, secure cookies, HSTS
"""

from .base import *
from decouple import config

# Turn off debug mode - NEVER run production with DEBUG=True!
# Debug mode exposes sensitive information in error pages
DEBUG = False

# Only allow requests from these domains
# .railway.app allows any Railway subdomain during deployment
ALLOWED_HOSTS = [
    'anthonybronkema.com',
    'www.anthonybronkema.com',
    '.railway.app',  # Railway deployment domains
]

# Get secret key from environment variable
# Generate a new one for production: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = config('SECRET_KEY')


# WhiteNoise configuration for serving static files
# Insert after SecurityMiddleware for optimal performance
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Use WhiteNoise's compressed manifest static files storage
# This adds cache-busting hashes to filenames and compresses files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Directory where collectstatic will collect all static files
# Railway will run: python manage.py collectstatic --noinput
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Security settings for production
# These ensure your site only works over HTTPS

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Only send session cookie over HTTPS
SESSION_COOKIE_SECURE = True

# Only send CSRF cookie over HTTPS
CSRF_COOKIE_SECURE = True

# HTTP Strict Transport Security (HSTS)
# Tells browsers to only connect via HTTPS for the next year
SECURE_HSTS_SECONDS = 31536000  # 1 year

# Include subdomains in HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Preload HSTS (optional, requires domain submission to browser vendors)
# SECURE_HSTS_PRELOAD = True


# Database configuration
# For now, using SQLite (same as development)
# Later, you might switch to PostgreSQL provided by Railway:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('PGDATABASE'),
#         'USER': config('PGUSER'),
#         'PASSWORD': config('PGPASSWORD'),
#         'HOST': config('PGHOST'),
#         'PORT': config('PGPORT', default='5432'),
#     }
# }
