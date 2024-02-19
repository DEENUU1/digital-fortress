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

    def num_of_user_projects(self, user) -> int:
        return self._model.objects.filter(user=user).count()

    def get_storage_info(self, _id: int):
        obj = self.get_by_id(_id)
        if obj:
            return obj.current_storage, obj.limit_storage
        return None, None
