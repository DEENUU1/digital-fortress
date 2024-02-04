from typing import Dict, Optional, List

from scenario.repository.project import ProjectRepository
from ..models import Project


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create(self, data: Dict) -> Project:
        return self._repository.create(data)

    def update(self, _id: int, data: Dict) -> Project:
        return self._repository.update(_id, data)

    def delete(self, _id: int) -> None:
        return self._repository.delete(_id)

    def get_by_slug(self, slug: str) -> Optional[Project]:
        return self._repository.get_by_slug(slug)

    def get_all(self) -> List[Optional[Project]]:
        return self._repository.get_all()

    def has_root_scenario(self, _id: int) -> bool:
        return self._repository.has_root(_id)
