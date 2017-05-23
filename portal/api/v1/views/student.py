import json

from django.http import HttpResponse

from api_base_view import APIBaseView
from api.v1.models.student import Student

class StudentView(APIBaseView):
    """
    API end point to perform queries on Student collection.
    """
    http_method_names = ['get', 'post']

    def post(self, request):
        print request.body

    def get(self, request, **kwargs):
        return self._process_get(Student, **kwargs)