from .base import *


# .config_secret 폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']

DEBUG = True
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".herokuapp.com"
]

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
