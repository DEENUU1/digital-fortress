from file.repository.file import FileRepository
from scenario.repository.project import ProjectRepository
from file.tasks import process_uploaded_file


class FileService:

    def __init__(self, repository: FileRepository):
        self._repository = repository

    def create(self, data):
        self._validate_file(data['file'])
        self._check_project_storage(data['project'].id, data["file"])

        instance = self._repository.create(data)

        # Run task to process file
        #
        # Split file into chunks and then save to pinecone vector database
        #
        # Todo add delay
        process_uploaded_file(instance, instance.user.id)

        return instance

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_all(self, user, project_id):
        return self._repository.get_all_per_project(user, project_id)

    @staticmethod
    def convert_file_size_to_mb(file_size: float) -> float:
        file_size_kb = file_size / 1024
        file_size_mb = file_size_kb / 1024
        return file_size_mb

    @staticmethod
    def _check_project_storage(project_id: int, uploaded_file) -> bool:
        project_repo = ProjectRepository()
        current_storage, limit_storage = project_repo.get_storage_info(project_id)

        file_size_mb = FileService.convert_file_size_to_mb(uploaded_file.size)

        if current_storage + file_size_mb > limit_storage:
            return False
        return True

    @staticmethod
    def _validate_file(file) -> bool:
        _VALID_EXTENSIONS = [".pdf", ".csv", ".json", ".md", ".txt"]
        for extension in _VALID_EXTENSIONS:
            if file.name.endswith(extension):
                return True
            return False
