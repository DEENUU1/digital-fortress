from .models import File
from rest_framework.serializers import ModelSerializer


class InputFileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = ("user", "file", "project")


class OutputFileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ("user", "file", "status", "created_at", "updated_at")
