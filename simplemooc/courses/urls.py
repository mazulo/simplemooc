from django.conf.urls import url
from simplemooc.courses import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^cursos/trb/$',
        views.list_courses_trb,
        name='list_courses_trb'
    ),
    url(
        r'^cursos/normal/$',
        views.list_courses_normal,
        name='list_courses_normal'
    ),
    url(
        r'^curso/(?P<pk>\d+)/$',
        views.course,
        name='course'
    ),
    url(
        r'^curso/(?P<pk>\d+)/create_lesson/$',
        views.create_lesson_trb,
        name='create_lesson_trb'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/$',
        views.details,
        name='details'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/inscricao/$',
        views.enrollment,
        name='enrollment'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$',
        views.undo_enrollment,
        name='undo_enrollment'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/anuncios/$',
        views.announcements,
        name='announcements'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$',
        views.show_announcement,
        name='show_announcement'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/aulas/$',
        views.lessons,
        name='lessons'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$',
        views.lesson,
        name='lesson'
    ),
    url(
        r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$',
        views.material,
        name='material'
    ),
]
