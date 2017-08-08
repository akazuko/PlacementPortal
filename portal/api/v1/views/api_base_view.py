import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class APIBaseView(APIView):
    """
    Base API View.
    """

    meta = {
        'abstract': True
    }

    model_cls = None
    serializer_cls = None

    def get(self, request, **kwargs):
        key = kwargs.get('key', None)

        if key:
            result = self.model_cls.find(key=key, value=kwargs['value'])
        else:
            result = self.model_cls.find()
        result = [json.loads(res.to_json()) for res in result]
        serializer = self.serializer_cls(result, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_cls(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, key, value):
        if key != 'id':
            return Response(data='usage: [DELETE] /api/v1/%s/id=$oid" %(repr(self))',
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            obj = self.model_cls.objects(id=value)
            obj.delete()
        except:
            return Response(data="Valid student $oid is not provided", status=status.HTTP_400_BAD_REQUEST)
        return Response(data="Data successfully deleted", status=status.HTTP_200_OK)

    def put(self, request, key, value):
        if key != 'id':
            return Response(data="Correct usage : [PUT] /api/v1/%s/id=$oid" %(repr(self)),
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            # get the required object
            obj = self.model_cls.objects(id=value)

            # here we get the list as result, but we need only the object
            obj = obj[0]
        except:
            return Response(data="Invalid id provided", status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_cls(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
