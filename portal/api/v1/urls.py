from django.conf.urls import url

from api.v1.views.student import StudentView
from api.v1.views.company import CompanyView
from api.v1.views.resume import ResumeView

app_name = 'api.v1'

urlpatterns = [
    url(r'^student/$', StudentView.as_view()),
    url(r'^student/(?P<key>\w+)=(?P<value>\w+)$', StudentView.as_view()),
    url(r'^company/$', CompanyView.as_view()),
    url(r'^company/(?P<key>\w+)=(?P<value>\w+)$', CompanyView.as_view()),
    url(r'^resume/$', ResumeView.as_view()),
    url(r'^resume/(?P<key>\w+)=(?P<value>\w+)$', ResumeView.as_view())
]