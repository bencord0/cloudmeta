from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from cloudmeta.apps.userdata import views

urlpatterns = patterns('',
    url(r'^$', views.user_data, name='user_data'),
)

