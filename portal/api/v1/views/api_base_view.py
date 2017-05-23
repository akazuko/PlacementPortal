import json

from django.http import HttpResponse
from django.views import View

class APIBaseView(View):
    """
    Base API View.
    """

    meta = {
        'abstract': True
    }

    def _process_get(self, cls, **kwargs):
        key = kwargs.get('key', None)

        if key:
            result = cls.find(key=key, value=kwargs['value'])
        else:
            result = cls.find()
        result = [json.loads(res.to_json()) for res in result]
        return HttpResponse(json.dumps(result, indent=2))