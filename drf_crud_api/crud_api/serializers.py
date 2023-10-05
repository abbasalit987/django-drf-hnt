from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    email = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=16)
    address = serializers.CharField(max_length=128)
    city = serializers.CharField(max_length=64)
    state = serializers.CharField(max_length=64)
    pincode = serializers.CharField(max_length=16)

    # def create(self, validated_data):
    #     return super().create(**validated_data)

    # def update(self, instance, validated_data):
    #     return super().update(instance, **validated_data)

    # def _read_only_defaults(self):
    #     return super()._read_only_defaults()
