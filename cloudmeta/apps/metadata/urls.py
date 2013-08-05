from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from cloudmeta.apps.metadata import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^hostname$', views.hostname, name='hostname'),
    url(r'^public-keys/(?P<idx>\d+)/openssh-key$', views.openssh_key, name='openssh_key'),
)

