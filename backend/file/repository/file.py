from core.repository.base_repository import CRUDRepository
from ..models import File
from rest_framework.exceptions import NotFound


class FileRepository(CRUDRepository):
    def __init__(self):
        super().__init__(File)

    def update_status(self, file_id, status):
        if not self.exists(file_id):
            raise NotFound(f"Object with id {file_id} does not exist")

        file = self.get_by_id(file_id)
        file.status = status
        file.save()
        return file
