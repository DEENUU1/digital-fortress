from ..models import Scenario
from scenario.repository.scenario import ScenarioRepository
from typing import Dict, Optional, List
from ..serializers import OutputScenarioSerializer, InputScenarioSerializer


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, request) -> Dict:
        serializer = InputScenarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        data["user"] = request.user

        scenario = self._repository.create(data)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data

    def delete(self, _id: int) -> None:
        self._repository.delete(_id)

    def get_all(self) -> List[Dict]:
        scenario = self._repository.get_all()
        serializer = OutputScenarioSerializer(scenario, many=True)
        return serializer.data

    def get_root(self, project_id: int) -> Dict:
        scenario = self._repository.get_root(project_id)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data

    def get_full_path(self, _id: int) -> List[Dict]:
        scenario = self._repository.get_full_path(_id)
        serializer = OutputScenarioSerializer(scenario, many=True)
        return serializer.data

    def has_root(self, project_id: int) -> bool:
        root = self.get_root(project_id)
        return root is not None

    def get_by_id(self, _id: int) -> Dict:
        scenario = self._repository.get_by_id(_id)
        serializer = OutputScenarioSerializer(scenario)
        return serializer.data
