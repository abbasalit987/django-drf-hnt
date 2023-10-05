from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Record
from .serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.


def recordAPI(request):
    if request.method == "GET":
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id', None)

        if id is not None:
            record = Record.objects.get(id=id)
            serializer = RecordSerializer(record)
        else:
            record = Record.objects.all()
            serializer = RecordSerializer(record, many=True)

        jsonData = JSONRenderer().render(serializer.data)
        return HttpResponse(jsonData, content_type='application/json')
