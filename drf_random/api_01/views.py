from django.shortcuts import render
from .models import Record
from .serializers import RecordSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.


def recordsData(request, pk):
    record = Record.objects.get(id=pk)
    serializer = RecordSerializer(record)
    # jsonData = JSONRenderer().render(serializer.data)
    # return HttpResponse(jsonData, content_type='application/json')
    return JsonResponse(serializer.data)


def recordsList(request):
    records = Record.objects.all()
    serializer = RecordSerializer(records, many=True)
    # jsonData = JSONRenderer().render(serializer.data)
    # return HttpResponse(jsonData, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
