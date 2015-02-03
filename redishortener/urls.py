from django.conf.urls import patterns, include, url
import settings
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'redishortener.views.index', name='index'),
    url(r'(P<long_url>[\w.@+-,\' \'\';\'%{}\[\]]+)?$', 'redishortener.views.follow', name='follow'),
)
