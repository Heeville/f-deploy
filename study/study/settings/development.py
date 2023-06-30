from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "3.35.8.16"
    ] #도메인,IP


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

STATIC_URL="static/"
STATIC_ROOT=BASE_DIR/"static"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}