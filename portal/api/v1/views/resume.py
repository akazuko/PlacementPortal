from api_base_view import APIBaseView
from api.v1.models.resume import Resume

class ResumeView(APIBaseView):
    """
    API end point to perform queries on Resume collection.
    """
    http_method_names = ['get', 'post', 'delete']

    def __repr__(self):
        return "resume"

    def post(self, request):
        return self._base_post(request, Resume)

    def get(self, request, **kwargs):
        return self._base_get(Resume, **kwargs)

    def delete(self, request, key, value):
        return self._base_delete(request, key, value, Resume)

    def put(self, request, key, value):
        return self._base_put(request, key, value, Resume)