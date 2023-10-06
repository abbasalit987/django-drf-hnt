from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Record
from .serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
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

    if request.method == "POST":
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        serializer = RecordSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            resMsg = {'msg': 'Data creation successfull'}
            jsonData = JSONRenderer().render(resMsg)
            return HttpResponse(jsonData, content_type='application/json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')

    if request.method == "PUT":
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        id = pythonData.get('id')
        record = Record.objects.get(id=id)
        serializer = RecordSerializer(record, data=pythonData, partial=True)
        if serializer.is_valid():
            serializer.save()
            resMsg = {'msg': 'Data updated successfully'}
            jsonData = JSONRenderer().render(resMsg)
            return HttpResponse(jsonData, content_type='application/json')
        jsonData = JSONRenderer().render(serializer.errors)
        return HttpResponse(jsonData, content_type='application/json')
