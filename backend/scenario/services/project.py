from scenario.repository.project import ProjectRepository
from subscription.repository.user_subscription import UserSubscriptionRepository


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create(self, data, user):
        if not self.check_max_project_limit(user):
            raise Exception("Max project limit reached")

        return self._repository.create(data)

    def update(self, data, project_id: int, user=None):
        return self._repository.update(project_id, data, user)

    def delete(self, user, _id: int) -> None:
        self._repository.delete(_id, user)

    def get_by_id(self, user, _id: int):
        return self._repository.get_by_id(_id, user)

    def get_all(self, user):
        return self._repository.get_all(user)

    def check_max_project_limit(self, user) -> bool:
        user_subscription_repo = UserSubscriptionRepository()
        user_subscription_product = user_subscription_repo.get_user_subscription(user.id)
        num_of_projects = self._repository.num_of_user_projects(user)

        if num_of_projects >= user_subscription_product.num_of_projects:
            return False
        return True
