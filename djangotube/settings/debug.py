from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'djangotube.wsgi.debug.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangotube',
        'USER': 'postgres',
        'PASSWORD': 'qhanf1gh',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    }
}
