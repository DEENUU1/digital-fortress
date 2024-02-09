from scenario.repository.scenario import ScenarioRepository
from scenario.repository.project import ProjectRepository
from typing import Dict, List
from ..serializers import OutputScenarioSerializer, InputScenarioSerializer


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, data):
        return self._repository.create(data)

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_all(self, user, project_slug: str):
        return self._repository.get_tree(project_slug, user)

    def has_root(self, user, project_id: int) -> bool:
        root = self._repository.get_root(project_id, user)
        return root is not None

    def get_by_id(self, user, _id: int):
        return self._repository.get_by_id(_id, user)
