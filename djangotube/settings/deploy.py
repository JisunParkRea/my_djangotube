from .base import *
import dj_database_url
import django_heroku

django_heroku.settings(locals())

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'djangotube.wsgi.deploy.application'

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
