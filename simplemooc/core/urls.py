from django.conf.urls import patterns, url


urlpatterns = patterns(
    'simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)
