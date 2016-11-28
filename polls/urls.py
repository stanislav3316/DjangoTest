from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<course_id>[0-9]+)/$', views.details, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<course_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^add/$', views.add, name='add'),
    url(r'^remove/(?P<course_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^removeStudent/(?P<student_id>[0-9]+)/course/(?P<course_id>[0-9]+)/$',
        views.deleteStudent, name='deleteStudent'),

    url(r'^edit/(?P<course_id>[0-9]+)$', views.editCourse, name='edit'),
    url(r'^updateCourse/(?P<course_id>[0-9]+)$', views.updateCourse, name='updateCourse'),
    url(r'^editStu/(?P<student_id>[0-9]+)$', views.editStudent, name='editStu'),
    url(r'^updateStudent/(?P<student_id>[0-9]+)/$', views.updateStudent, name='updateStu')
]