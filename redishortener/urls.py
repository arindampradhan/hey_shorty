from django.conf.urls import patterns, include, url
import settings
from .api import UrlResource
from django.views.generic import RedirectView
from django.views.generic import TemplateView

url_resource = UrlResource()


urlpatterns = patterns('',
    url(r'api/',include(url_resource.urls)),
    url(r'^$', 'redishortener.views.index', name='index'),
    url(r'(P<long_url>[\w.@+-,\' \'\';\'%{}\[\]]+)?$', 'redishortener.views.follow', name='follow'),
)
