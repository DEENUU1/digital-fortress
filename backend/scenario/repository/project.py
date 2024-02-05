from core.repository.base_repository import CRUDRepository
from ..models import Project


class ProjectRepository(CRUDRepository):
    def __init__(self):
        super().__init__(Project)

    def update_current_storage(self, _id: int, value: float, user=None) -> bool:
        obj = self.get_by_id(_id, user)
        if obj:
            obj.current_storage += value
            obj.save()
            return True

        return False
