from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(
        r'^entrar/$',
        'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'},
        name='login'
    ),
    url(r'^cadastre-se/$',
        'simplemooc.accounts.views.register', name='register'),
)
