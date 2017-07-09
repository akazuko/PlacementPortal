from django.conf.urls import url

from api.v1.views.student import StudentView

app_name = 'api.v1'

urlpatterns = [
    url(r'^student/$', StudentView.as_view()),
    url(r'^student/(?P<key>[a-z0-9]+)=(?P<value>[a-z0-9]+)$', StudentView.as_view())
]