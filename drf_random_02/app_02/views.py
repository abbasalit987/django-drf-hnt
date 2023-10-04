from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def createRecords(request):
    if request.method == "POST":
        jsonData = request.body
        stream = io.BytesIO(jsonData)
        pythonData = JSONParser().parse(stream)
        serializer = RecordSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            responseData = {'msg': 'Data creation successful'}
            responseJsonData = JSONRenderer().render(responseData)
            return HttpResponse(responseJsonData, content_type='application/json')
