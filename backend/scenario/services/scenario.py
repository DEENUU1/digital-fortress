from scenario.repository.scenario import ScenarioRepository
from scenario.repository.project import ProjectRepository
from typing import Dict, List
from ..serializers import OutputScenarioSerializer, InputScenarioSerializer


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, data, user) -> Dict:
        serializer = InputScenarioSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        serialized_data = serializer.data["user"] = user

        data["project"] = ProjectRepository().get_by_id(serialized_data["project"], user)
        data["parent_id"] = self._repository.get_by_id(serialized_data["parent_id"], user)

        scenario = self._repository.create(serialized_data)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_all(self, user, project_id: int) -> List[Dict]:
        scenario = self._repository.get_tree(project_id, user)
        serializer = OutputScenarioSerializer(scenario, many=True)
        return serializer.data

    def has_root(self, user, project_id: int) -> bool:
        root = self._repository.get_root(project_id, user)
        return root is not None

    def get_by_id(self, user, _id: int) -> Dict:
        scenario = self._repository.get_by_id(_id, user)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data
