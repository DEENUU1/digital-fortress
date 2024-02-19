from .models import File
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class InputFileSerializer(ModelSerializer):
    # file = serializers.FileField()
    class Meta:
        model = File
        fields = ("user", "file", "project")


class OutputFileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ("user", "file", "status", "created_at", "updated_at")
