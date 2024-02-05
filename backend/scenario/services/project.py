from typing import Dict, List

from scenario.repository.project import ProjectRepository
from user.models import UserAccount
from ..serializers import OutputProjectSerializer, InputProjectSerializer


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create(self, request) -> Dict:
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        data = request.data
        data["user"] = user

        project = self._repository.create(data)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def update(self, request, project_id: int) -> Dict:
        serializer = InputProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data

        project = self._repository.update(project_id, data)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def delete(self, _id: int) -> None:
        self._repository.delete(_id)

    def get_by_slug(self, slug: str) -> Dict:
        project = self._repository.get_by_slug(slug)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def get_all(self) -> List[Dict]:
        projects = self._repository.get_all()
        serializer = OutputProjectSerializer(projects, many=True)
        return serializer.data
