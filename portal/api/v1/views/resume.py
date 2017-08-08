from api_base_view import APIBaseView
from api.v1.models.resume import Resume
from api.v1.serializer import ResumeSerializer

class ResumeView(APIBaseView):
    """
    API end point to perform queries on Resume collection.
    """
    http_method_names = ['get', 'post', 'delete', 'put']

    model_cls = Resume
    serializer_cls = ResumeSerializer

    def __repr__(self):
        return "resume"
