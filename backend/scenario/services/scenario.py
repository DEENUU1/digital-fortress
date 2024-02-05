from scenario.repository.scenario import ScenarioRepository
from scenario.repository.project import ProjectRepository
from typing import Dict, List
from ..serializers import OutputScenarioSerializer, InputScenarioSerializer


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, request) -> Dict:
        serializer = InputScenarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        data["user"] = request.user

        data["project"] = ProjectRepository().get_by_id(data["project"], request.user)
        data["parent_id"] = self._repository.get_by_id(data["parent_id"], request.user)

        scenario = self._repository.create(data)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data

    def delete(self, request, _id: int) -> None:
        self._repository.delete(_id, request.user)

    def get_all(self, request, project_id: int) -> List[Dict]:
        scenario = self._repository.get_tree(project_id, request.user)
        serializer = OutputScenarioSerializer(scenario, many=True)
        return serializer.data

    def get_full_path(self, _id: int) -> List[Dict]:
        scenario = self._repository.get_full_path(_id)
        serializer = OutputScenarioSerializer(scenario, many=True)
        return serializer.data

    def has_root(self, request, project_id: int) -> bool:
        root = self._repository.get_root(project_id, request.user)
        return root is not None

    def get_by_id(self, request, _id: int) -> Dict:
        scenario = self._repository.get_by_id(_id, request.user)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data
