from typing import Dict, List

from scenario.repository.project import ProjectRepository
from ..serializers import OutputProjectSerializer, InputProjectSerializer
from subscription.repository.user_subscription import UserSubscriptionRepository


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create(self, request) -> Dict:
        if not self.check_max_project_limit(request):
            raise Exception("Max project limit reached")

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

        project = self._repository.update(project_id, data, request.user)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def delete(self, request, _id: int) -> None:
        self._repository.delete(_id, request.user)

    def get_by_id(self, request, _id: int) -> Dict:
        project = self._repository.get_by_id(_id, request.user)
        serializer = OutputProjectSerializer(project)
        return serializer.data

    def get_all(self, request) -> List[Dict]:
        projects = self._repository.get_all(request.user)
        serializer = OutputProjectSerializer(projects, many=True)
        return serializer.data

    def check_max_project_limit(self, request) -> bool:
        user_subscription_repo = UserSubscriptionRepository()
        user_subscription_product = user_subscription_repo.get_user_subscription(request.user.id)
        num_of_projects = self._repository.num_of_user_projects(request.user)

        if num_of_projects >= user_subscription_product.num_of_projects:
            return False
        return True
