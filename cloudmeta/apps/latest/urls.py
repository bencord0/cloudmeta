from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from cloudmeta.apps.latest import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^meta-data/hostname$', views.hostname, name='hostname'),
    url(r'^meta-data/public-keys/(?P<idx>\d+)/openssh-key$', views.sshkey, name='sshkey'),
    url(r'^user-data/$', views.userdata, name='userdata'),
)
