"""
Definition of urls for lukyanov.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin

import app.forms
import app.views

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^exit/$',app.views.exit,name='exit'),
    url(r'^skyway$',app.views.skyway, name='skyway'),
    url(r'^article/(\d+)/$',app.views.articles,name='articles'),
    url(r'^page/(\d+)/$',app.views.main, name='article'),
    url(r'^adminpanel/delete$',app.views.delete,name='delete'),
    url(r'^adminpanel/$',app.views.adminpanel,name='adminpanel'),
    url(r'^$', app.views.main, name='main'),
    url(r'^about/$', app.views.about, name='about'),
    url(r'^login/$', app.views.login,name='login'),
    url(r'^copyrighting/$', app.views.cop, name='cop'),
    url(r'^registration/$',app.views.registration, name='registration'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
