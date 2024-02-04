from ..models import Scenario
from scenario.repository.scenario import ScenarioRepository
from typing import Dict, Optional, List


class ScenarioService:

    def __init__(self, repository: ScenarioRepository):
        self._repository = repository

    def create(self, data: Dict):
        return self._repository.create(data)

    def update(self, _id: int, data: Dict) -> Scenario:
        return self._repository.update(_id, data)

    def delete(self, _id: int) -> None:
        return self._repository.delete(_id)

    def get_all(self) -> List[Optional[Scenario]]:
        return self._repository.get_all()

