"""
Base Django settings for config project.

This file contains settings that are shared across all environments
(development, production, etc.). Environment-specific settings are
in separate files that import from this base.

Learning concepts:
- Settings organization: Splitting settings by environment
- SECRET_KEY: Used for cryptographic signing (sessions, cookies, tokens)
- INSTALLED_APPS: Django apps that are active in this project
- MIDDLEWARE: Processing layers for requests/responses
- TEMPLATES: How Django finds and renders HTML templates
- STATIC_URL: URL prefix for serving static files (CSS, JS, images)
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR points to the project root (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# This default key is for development only. Production will override this.
SECRET_KEY = 'django-insecure-b-^7x%gjugpbq_d1&casky5md5(6$6q9e1^+!0@ej0(#-ucgmk'

# SECURITY WARNING: don't run with debug turned on in production!
# This will be overridden in production settings
DEBUG = True

# Hosts/domain names that Django will serve
# This will be overridden in environment-specific settings
ALLOWED_HOSTS = []


# Application definition
# Django apps enabled for this project
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',        # Admin interface
    'django.contrib.auth',         # Authentication system
    'django.contrib.contenttypes', # Content type system
    'django.contrib.sessions',     # Session framework
    'django.contrib.messages',     # Messaging framework
    'django.contrib.staticfiles',  # Static file management

    # Your custom apps
    'portfolio.apps.PortfolioConfig',  # Portfolio app
]

# Middleware is processed in order for requests (top to bottom)
# and in reverse for responses (bottom to top)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration module
ROOT_URLCONF = 'config.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Directories to search for templates before looking in apps
        'DIRS': [BASE_DIR / 'portfolio' / 'templates'],
        # APP_DIRS: Whether to look for templates in each app's templates/ directory
        'APP_DIRS': True,
        'OPTIONS': {
            # Context processors add variables to every template context
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application used by Django's runserver and production servers
WSGI_APPLICATION = 'config.wsgi.application'


# Database
# Environment-specific settings will override this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# URL prefix for static files (e.g., /static/portfolio/css/main.css)
STATIC_URL = '/static/'

# Additional locations of static files beyond app directories
# In development, Django will serve files from here automatically
STATICFILES_DIRS = [
    BASE_DIR / 'portfolio' / 'static',
]

# Directory where collectstatic will gather all static files for production
# This is set in production settings
# STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
