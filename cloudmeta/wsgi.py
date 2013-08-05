"""
WSGI config for cloudmeta project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cloudmeta.settings.dev")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

# See: https://github.com/kennethreitz/dj-static/blob/master/README.rst
from dj_static import Cling
application = Cling(application)

def main():
    from django.core import management
    from django.conf import settings

    PORT = os.environ.get('PORT', 8000)

    management.call_command('syncdb', interactive=False, migrate=True)
    management.call_command('collectstatic', interactive=False)

    if 'gunicorn' in settings.INSTALLED_APPS:
        management.call_command('run_gunicorn', '[::]:{PORT}'.format(PORT=PORT))
    else:
        management.call_command('runserver', '[::]:{PORT}'.format(PORT=PORT))

if __name__ == '__main__':
    main()
