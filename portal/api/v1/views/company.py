from api_base_view import APIBaseView
from api.v1.models.company import Company
from api.v1.serializer import CompanySerializer

class CompanyView(APIBaseView):
    """
    API end point to perform queries on Company collection.
    """
    http_method_names = ['get', 'post', 'delete', 'put']

    model_cls = Company
    serializer_cls = CompanySerializer

    def __repr__(self):
        return "company"
