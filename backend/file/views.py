from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository.file import FileRepository
from .serializers import InputFileSerializer, OutputFileSerializer
from .services.file import FileService


class FileUploadAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    _service = FileService(FileRepository())

    @swagger_auto_schema(operation_description="Add file", request_body=InputFileSerializer)
    def post(self, request):
        serializer = InputFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self._service.create(serializer.validated_data)
        return Response(OutputFileSerializer(instance).data, status=status.HTTP_201_CREATED)


class FileListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    _service = FileService(FileRepository())

    def get(self, request, project_id: int):
        instance = self._service.get_all(request.user, project_id)
        return Response(OutputFileSerializer(instance, many=True).data, status=status.HTTP_200_OK)
