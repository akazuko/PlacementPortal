from api_base_view import APIBaseView
from api.v1.models.student import Student
from api.v1.serializer import StudentSerializer

class StudentView(APIBaseView):
    """
    API end point to perform queries on Student collection.
    """
    http_method_names = ['get', 'post', 'delete', 'put']

    model_cls = Student
    serializer_cls = StudentSerializer

    def __repr__(self):
        return "student"
