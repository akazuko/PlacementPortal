from api_base_view import APIBaseView
from api.v1.models.student import Student

class StudentView(APIBaseView):
    """
    API end point to perform queries on Student collection.
    """
    http_method_names = ['get', 'post', 'delete']

    def __repr__(self):
        return "student"

    def post(self, request):
        return self._base_post(request, Student)

    def get(self, request, **kwargs):
        return self._base_get(Student, **kwargs)

    def delete(self, request, key, value):
        return self._base_delete(request, key, value, Student)

    def put(self, request, key, value):
        return self._base_put(request, key, value, Student)