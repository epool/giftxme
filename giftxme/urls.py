from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from comingsoon import views

urlpatterns = patterns('',
    url(r'', views.index),
    # Examples:
    # url(r'^$', 'giftxme.views.home', name='home'),
    # url(r'^giftxme/', include('giftxme.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^giftexchange/', include('giftexchange.urls', namespace="giftexchange")),
)
