import os
import uuid
import dj_database_url

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {'default': dj_database_url.config(
    default='sqlite:///{}/sqlite.db'.format(BASE_DIR))}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',

    'cloudmeta.apps.latest',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

ROOT_URLCONF = 'cloudmeta.urls'

SECRET_KEY = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

STATIC_ROOT=os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

