from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository import project as project_repo, scenario as scenario_repo
from .services import project as project_service, scenario as scenario_service
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    InputProjectSerializer,
    InputScenarioSerializer,
    OutputScenarioSerializer,
    OutputProjectSerializer
)


class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request):
        instance = self._service.get_all(request)
        return Response(OutputProjectSerializer(instance, many=True).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create new project", request_body=InputProjectSerializer)
    def post(self, request):
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self._service.create(serializer.validated_data, request.user)
        return Response(OutputProjectSerializer(instance).data, status=status.HTTP_201_CREATED)


class ProjectDetailDeleteUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request, pk: int):
        instance = self._service.get_by_id(request.user, pk)
        return Response(OutputProjectSerializer(instance).data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        self._service.delete(request.user, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_description="Update project", request_body=InputProjectSerializer)
    def put(self, request, pk: int):
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self._service.update(serializer.validated_data, pk, request.user)
        return Response(OutputProjectSerializer(instance).data, status=status.HTTP_200_OK)


class ScenarioCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    @swagger_auto_schema(operation_description="Create new scenario", request_body=InputScenarioSerializer)
    def post(self, request):
        serializer = InputScenarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self._service.create(serializer.validated_data)
        return Response(OutputScenarioSerializer(instance).data, status=status.HTTP_201_CREATED)


class ScenarioTreeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, project_id: int):
        instances = self._service.get_all(request.user, project_id)
        return Response(OutputScenarioSerializer(instances, many=True).data, status=status.HTTP_200_OK)


class ScenarioDetailDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, pk: int):
        instance = self._service.get_by_id(request.user, pk)
        return Response(OutputScenarioSerializer(instance).data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        self._service.delete(request.user, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScenarioHasRootAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, project_id: int):
        root = self._service.has_root(request.user, project_id)
        if root:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
