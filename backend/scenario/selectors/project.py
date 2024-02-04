from rest_framework.exceptions import ValidationError

from scenario.models import Project, Scenario
from typing import List


class ProjectSelector:

    def list(self) -> List[Project]:
        return Project.objects.all()

    def get(self, project_slug: str) -> Project:
        exists = Project.objects.filter(slug=project_slug).exists()
        if not exists:
            raise ValidationError(f'Project {project_slug} does not exist')
        return Project.objects.filter(slug=project_slug).first()

    def has_root(self, project_slug: str) -> bool:
        return Scenario.objects.filter(project__slug=project_slug, parent_id=None).exists()
