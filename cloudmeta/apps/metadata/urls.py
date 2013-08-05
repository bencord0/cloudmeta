from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from cloudmeta.apps.metadata import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

