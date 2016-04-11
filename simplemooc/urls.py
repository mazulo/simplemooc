from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^contas/', include(
        'simplemooc.accounts.urls', namespace='accounts')),
    url(r'^forum/', include('simplemooc.forum.urls', namespace='forum')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
