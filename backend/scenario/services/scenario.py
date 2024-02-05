from ..models import Scenario
from scenario.repository.scenario import ScenarioRepository
from typing import Dict, Optional, List


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, data: Dict):
        return self._repository.create(data)

    def delete(self, _id: int) -> None:
        return self._repository.delete(_id)

    def get_all(self) -> List[Optional[Scenario]]:
        return self._repository.get_all()

    def get_root(self, project_id: int) -> Optional[Scenario]:
        return self._repository.get_root(project_id)

    def get_full_path(self, _id: int) -> List[Optional[Scenario]]:
        return self._repository.get_full_path(_id)

    def has_root(self, project_id: int) -> bool:
        root = self.get_root(project_id)
        return root is not None
