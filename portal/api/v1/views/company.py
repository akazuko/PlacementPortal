from api_base_view import APIBaseView
from api.v1.models.company import Company

class CompanyView(APIBaseView):
    """
    API end point to perform queries on Company collection.
    """
    http_method_names = ['get', 'post', 'delete']

    def __repr__(self):
        return "company"

    def post(self, request):
        return self._base_post(request, Company)

    def get(self, request, **kwargs):
        return self._base_get(Company, **kwargs)

    def delete(self, request, key, value):
        return self._base_delete(request, key, value, Company)

    def put(self, request, key, value):
        return self._base_put(request, key, value, Company)