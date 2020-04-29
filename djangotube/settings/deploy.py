from .base import *
import dj_database_url
import django_heroku


django_heroku.settings(locals())

DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']

# WSGI application
WSGI_APPLICATION = 'djangotube.wsgi.deploy.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
