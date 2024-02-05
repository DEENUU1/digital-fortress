from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository import project as project_repo, scenario as scenario_repo
from .services import project as project_service, scenario as scenario_service
from .permissions import IsOwner
from drf_yasg.utils import swagger_auto_schema
from .serializers import InputProjectSerializer, InputScenarioSerializer


class ProjectListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request):
        projects = self._service.get_all(request)
        return Response(projects, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create new project", request_body=InputProjectSerializer)
    def post(self, request):
        project = self._service.create(request)
        return Response(project, status=status.HTTP_201_CREATED)


class ProjectDetailDeleteUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request, pk: int):
        project = self._service.get_by_id(request, pk)
        return Response(project, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        self._service.delete(request, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(operation_description="Update project", request_body=InputProjectSerializer)
    def put(self, request, pk: int):
        project = self._service.update(request, pk)
        return Response(project, status=status.HTTP_200_OK)


class ScenarioCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    @swagger_auto_schema(operation_description="Create new scenario", request_body=InputScenarioSerializer)
    def post(self, request):
        scenario = self._service.create(request)
        return Response(scenario, status=status.HTTP_201_CREATED)


class ScenarioTreeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, project_id: int):
        tree = self._service.get_all(request, project_id)
        return Response(tree, status=status.HTTP_200_OK)


class ScenarioDetailDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, pk: int):
        scenario = self._service.get_by_id(request, pk)
        return Response(scenario, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        self._service.delete(request, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScenarioHasRootAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, project_id: int):
        root = self._service.has_root(request, project_id)
        if root:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
