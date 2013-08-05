CloudMeta
=========

An independent metadata server for cloud systems.

CloudMeta is a standalone implementation of the server side API for Amazon's
AWS metadata server used to configure EC2 instances. This method of
bootstrapping cloudy virtual machines is the defacto method for cloud-init.


Usage
=====

    $ virtualenv --distribute cloudmeta && cd cloudmeta
    $ source ./bin/activate
    (cloudmeta)$ pip install -r requirements.txt
    (cloudmeta)$ pip intsall -e .
    (cloudmeta)$ cloudmeta

The server will now be listening on port 8000. Feel free to connect to it from a browser.

To login to the admin interface, you will need to create a super user.

    (cloudmeta)$ python manage.py createsuperuser

You only need to do this once per deployment.

The Admin Interface
===================


Configuration environment
=========================

All configuration is handled through environment variables.
A good way to store them locally is in a file that is never checked into
git. Conventionally, this is the .env file in the project root.

Tools like foreman (ruby) or honcho (python) will use the .env environment
when running processes described in the Procfile.

This convention is also supported by PaaSes like Heroku. Instead of storing
configuration variables in a file (which you should never add to source
control), heroku uses config vars.
(https://devcenter.heroku.com/articles/config-vars)

The rest of this sections describes variables that you should set.

SECRET_KEY
----------
While not strictly required, it is recommended to generate a secret key per
deployment.

     (cloudmeta)$ SECRET_KEY=$(python -c 'import random;
         print "".join([random.choice(
               "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
         ) for i in range(50)])')

for local deployments

     (cloudmeta)$ echo "SECRET_KEY=$SECRET_KEY" >> .env
     (cloudmeta)$ export $(cat .env)

for heroku

    (cloudmeta)$ heroku config:set "SECRET_KEY=$SECRET_KEY"

If SECRET_KEY is not provided from the environment, it will fallback
to a value which is automatically generated on startup.


DATABASE_URL
------------
It is also a good idea to use a dedicated database.
A PaaS like heroku will automatically provision a postgres DATABASE_URL.
A local sqlite database will be used if unset.

    (cloudmeta)$ DATABASE_URL=postgres://username:password@host:port/db_name


PORT
----
By default, the application will bind to port 8000. This can be overwritten
using the PORT environmental variable.

    (cloudmeta)$ PORT=5000

If running locally with foreman or honcho, a PORT will be picked for you.
Heroku will also use this PORT for local binding.


Local Dependencies
==================

Gentoo
------
Recompile python with USE=sqlite
Also install
	dev-python/virtualenv
	dev-db/postgresql-base
	dev-libs/libmemcached

Debian/Ubuntu
=============
???

Fedora
======
???

