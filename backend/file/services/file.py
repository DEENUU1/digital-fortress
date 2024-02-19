from file.repository.file import FileRepository
from scenario.repository.project import ProjectRepository


class FileService:

    def __init__(self, repository: FileRepository):
        self._repository = repository

    def create(self, data):
        self._validate_file(data['file'])
        size = 5
        self._check_project_storage(data['project'].id, size)
        return self._repository.create(data)

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_all(self, user):
        return self._repository.get_all(user)

    @staticmethod
    def _check_project_storage(project_id: int, file_size: float) -> bool:
        project_repo = ProjectRepository()
        current_storage, limit_storage = project_repo.get_storage_info(project_id)

        if current_storage + file_size > limit_storage:
            return False
        return True

    @staticmethod
    def _validate_file(file):
        if not file.name.endswith('.txt'):
            raise ValueError('Invalid file type')
