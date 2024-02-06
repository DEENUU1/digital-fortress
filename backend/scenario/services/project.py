from typing import Dict, List

from scenario.repository.project import ProjectRepository
from ..serializers import OutputProjectSerializer, InputProjectSerializer
from subscription.repository.user_subscription import UserSubscriptionRepository


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create(self, data, user) -> Dict:
        if not self.check_max_project_limit(user):
            raise Exception("Max project limit reached")

        serializer = InputProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        data["user"] = user

        project = self._repository.create(data)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def update(self, data, project_id: int, user) -> Dict:
        serializer = InputProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        project = self._repository.update(project_id, serializer.data, user)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_by_id(self, user, _id: int) -> Dict:
        project = self._repository.get_by_id(_id, user)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def get_all(self, user) -> List[Dict]:
        projects = self._repository.get_all(user)
        serializer = OutputProjectSerializer(projects, many=True)
        return serializer.data

    def check_max_project_limit(self, user) -> bool:
        user_subscription_repo = UserSubscriptionRepository()
        user_subscription_product = user_subscription_repo.get_user_subscription(user.id)
        num_of_projects = self._repository.num_of_user_projects(user)

        if num_of_projects >= user_subscription_product.num_of_projects:
            return False
        return True
