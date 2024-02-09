from typing import Optional, List

from core.repository.base_repository import CRUDRepository
from ..models import Scenario


class ScenarioRepository(CRUDRepository):
    def __init__(self):
        super().__init__(Scenario)

    def get_root(self, project_id: int, user) -> Optional[Scenario]:
        try:
            return self._model.objects.filter(project_id=project_id, parent_id__isnull=True, user=user).first()
        except self._model.DoesNotExist:
            return None

    def get_full_path(self, scenario_id: int) -> List[Optional[Scenario]]:
        path = []
        current_scenario = self._model.objects.filter(id=scenario_id).first()

        while current_scenario:
            path.append(current_scenario)
            current_scenario = current_scenario.parent_id

        return list(reversed(path))

    def get_tree(self, project_slug: str, user) -> List[Scenario]:
        return self._model.objects.filter(project__slug=project_slug, user=user).order_by('parent_id')
