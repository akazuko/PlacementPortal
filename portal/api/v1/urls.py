from django.conf.urls import url

from api.v1.views.student import StudentView
from api.v1.views.company import CompanyView
from api.v1.views.resume import ResumeView

app_name = 'api.v1'

urlpatterns = [
    url(r'^student/$', StudentView.as_view()),
    url(r'^student/(?P<key>[a-z0-9]+)=(?P<value>[a-z0-9]+)$', StudentView.as_view()),
    url(r'^company/$', CompanyView.as_view()),
    url(r'^company/(?P<key>[a-z0-9]+)=(?P<value>[a-z0-9]+)$', CompanyView.as_view()),
    url(r'^resume/$', ResumeView.as_view()),
    url(r'^resume/(?P<key>[a-z0-9]+)=(?P<value>[a-z0-9]+)$', ResumeView.as_view())
]