from rest_framework import serializers


class RecordSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    email = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    address = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=64)
    state = serializers.CharField(max_length=64)
    pincode = serializers.CharField(max_length=16)
