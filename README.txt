======
README
======

Usage
=====

    $ project="my_project_name"
    $ virtualenv --distribute ${project} && cd ${project}
    $ source ./bin/activate
    (project)$ pip install django
    (project)$ django-admin.py startproject --template=<path to this repo> ${project} .
    (project)$ pip install -r requirements.txt
    (project)$ pip intsall -e .
    (project)$ ${project}

The server will now be listening on port 8000. Feel free to connect to it from a browser.

To login to the admin interface, you will need to create a super user.

    (project)$ python manage.py createsuperuser

You only need to do this once per deployment.

Configuration environment
=========================

SECRET_KEY
----------
While not strictly required, it is also recommended to do

     $ SECRET_KEY=$(python -c 'import random;
         print "".join([random.choice(
               "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
         ) for i in range(50)])')
     $ heroku config:add SECRET_KEY=$SECRET_KEY

The production settings pull SECRET_KEY from environment but fallbacks
to a value which is generated mainly for development environment.

This setup allows you to easily keep your site in a public repo if you so 
wish without causing opening a route to attack your Django passwords.

DATABASE_URL
------------
It is also a good idea to use a dedicated database.

    $ DATABASE_URL=postgres://username:password@host:port/db_name

A local sqlite database will be used if unset.

PORT
----
By default, the application will bind to port 8000. This can be overwritten
using the PORT environmental variable. E.g. locally with foreman/honcho, or
on a PaaS like Heroku.

Dependencies
============

Gentoo
------
Recompile python with USE=sqlite
Also install
	dev-python/virtualenv
	dev-db/postgresql-base
	dev-libs/libmemcached

