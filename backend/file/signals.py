from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import File
from file.services.file import FileService
from file.repository.file import FileRepository
from scenario.repository.project import ProjectRepository


@receiver(post_save, sender=File)
def update_project_file_storage_after_uploading_file(sender, instance, created, **kwargs):
    if created:
        file_service = FileService(FileRepository())
        file_size_mb = file_service.convert_file_size_to_mb(instance.file.size)

        project_repository = ProjectRepository()
        project_repository.update_current_storage(instance.project.id, file_size_mb)


post_save.connect(update_project_file_storage_after_uploading_file, sender=File)
