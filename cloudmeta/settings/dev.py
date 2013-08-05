"""Development settings and globals."""


from os.path import join, normpath
from os import environ

########## DEBUG CONFIGURATION
environ.setdefault("DEBUG", "True")
########## END DEBUG CONFIGURATION

from common import *


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = [ iip.strip() for iip in environ.get('INTERNAL_IPS', '127.0.0.1').split(',')]

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION

