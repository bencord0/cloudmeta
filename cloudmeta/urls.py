from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Redirect / to admin
    url(r'^$', RedirectView.as_view(url='/admin/')),
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^latest/meta-data/', include('cloudmeta.apps.metadata.urls')),
    url(r'^latest/user-data/', include('cloudmeta.apps.userdata.urls')),
)
