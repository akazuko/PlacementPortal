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

    def _base_get(self, cls, **kwargs):
        key = kwargs.get('key', None)

        if key:
            result = cls.find(key=key, value=kwargs['value'])
        else:
            result = cls.find()
        result = [json.loads(res.to_json()) for res in result]
        return HttpResponse(json.dumps(result, indent=2))

    def _base_post(self, request, model_class):
        # convert the data to utf-8 format and the load the json.
        data = json.loads(request.body.decode('utf-8'))
        obj = model_class()

        # allow only data with the correct and valid keys to go through.
        for key in data:
            try:
                getattr(obj, str(key))
                setattr(obj, str(key), data[key])
            except:
                return HttpResponse("Wrong key: {key} provided".format(key=key),
                                    status=500)

        # above we checked for the right keys, this check ensures the correct
        # data -type for each key/field.
        try:
            obj.save()
        except:
            return HttpResponse("Please verify the input type for each field "
                                "properly".format(key=key), status=500)
        return HttpResponse("Data successfully added", status=200)

    def _base_delete(self, request, key, value, model_class):
        if key != 'id':
            return HttpResponse("Correct usage : [DELETE] /api/v1/%s/id=$oid" %(repr(model_class)),
                                status=500)
        try:
            obj = model_class.objects(id=value)
            obj.delete()
        except:
            return HttpResponse("Valid student $oid is not provided",
                                status=500)
        return HttpResponse("Data successfully deleted", status=200)

    def _base_put(self, request, key, value, model_class):
        if key != 'id':
            return HttpResponse("Correct usage : [PUT] /api/v1/%s/id=$oid" %(repr(model_class)),
                                status=500)
        try:
            data = json.loads(request.body.decode('utf-8'))
            if '_id' in data:
                id = data.pop('_id')
            elif 'id' in data:
                id = data.pop('id')

            # get the required object
            obj = model_class.objects(id=value)

            # allow only data with the correct and valid keys to go through.
            for key in data:
                try:
                    getattr(obj, str(key))
                    setattr(obj, str(key), data[key])
                except:
                    return HttpResponse(
                        "Wrong key: {key} provided".format(key=key),
                        status=500)

            # above we checked for the right keys, this check ensures the correct
            # data -type for each key/field.
            try:
                obj.save()
            except:
                return HttpResponse(
                    "Please verify the input type for each field "
                    "properly".format(key=key), status=500)
        except:
            return HttpResponse("Valid %s $oid is not provided" %(repr(model_class)),
                                status=500)
        return HttpResponse("Data successfully updated.", status=200)
