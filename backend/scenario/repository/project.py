from typing import Optional

from core.repository.base_repository import CRUDRepository
from ..models import Project, Scenario


class ProjectRepository(CRUDRepository):
    def __init__(self):
        super().__init__(Project)

    def get_by_slug(self, slug: str) -> Optional[Project]:
        try:
            return self._model.objects.get(slug=slug)
        except self._model.DoesNotExist:
            return None

    def update_current_storage(self, _id: int, value: float) -> bool:
        obj = self.get_by_id(_id)
        if obj:
            obj.current_storage += value
            obj.save()
            return True

        return False

    @staticmethod
    def has_root(_id: int) -> bool:
        return Scenario.objects.filter(project_id=_id, parent_id=None).exists()
