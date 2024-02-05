from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import (
    OutputProjectSerializer,
    OutputScenarioSerializer,
    InputProjectSerializer,
    InputScenarioSerializer
)
from .services import project as project_service, scenario as scenario_service
from .repository import project as project_repo, scenario as scenario_repo


class ProjectManagementAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request):
        projects = self._service.get_all()
        serializer = OutputProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        projects = self._service.create(serializer.data)
        return Response(projects, status=status.HTTP_201_CREATED)

    def delete(self, request, project_id: int):
        self._service.delete(project_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, project_id: int):
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        projects = self._service.update(project_id, serializer.data)
        return Response(projects, status=status.HTTP_200_OK)


class ProjectDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request, project_slug: str):
        project = self._service.get_by_slug(project_slug)
        serializer = OutputProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
