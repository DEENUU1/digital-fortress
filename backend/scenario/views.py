from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository import project as project_repo, scenario as scenario_repo
from .services import project as project_service, scenario as scenario_service


class ProjectManagementAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request):
        projects = self._service.get_all()
        return Response(projects, status=status.HTTP_200_OK)

    def post(self, request):
        project = self._service.create(request)
        return Response(project, status=status.HTTP_201_CREATED)

    def delete(self, request, project_id: int):
        self._service.delete(project_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, project_id: int):
        project = self._service.update(request, project_id)
        return Response(project, status=status.HTTP_200_OK)


class ProjectDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = project_service.ProjectService(project_repo.ProjectRepository())

    def get(self, request, project_slug: str):
        project = self._service.get_by_slug(project_slug)
        return Response(project, status=status.HTTP_200_OK)


class ScenarioManagementAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request):
        scenarios = self._service.get_all()
        return Response(scenarios, status=status.HTTP_200_OK)

    def post(self, request):
        scenario = self._service.create(request)
        return Response(scenario, status=status.HTTP_201_CREATED)

    def delete(self, request, scenario_id: int):
        self._service.delete(scenario_id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScenarioHasRootAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, project_id: int):
        root = self._service.get_root(project_id)
        if root:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ScenarioDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    _service = scenario_service.ScenarioService(scenario_repo.ScenarioRepository())

    def get(self, request, scenario_id: int):
        scenario = self._service.get_by_id(scenario_id)
        return Response(scenario, status=status.HTTP_200_OK)
