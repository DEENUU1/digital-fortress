from typing import Dict

from rest_framework.exceptions import ValidationError

from scenario.models import Project
from subscription.selectors.user_subscription import UserSubscriptionSelector
from user.models import UserAccount


class ProjectService:

    def create(self, user: UserAccount, data: Dict) -> Project:
        title = data.get("title", None)

        if not title:
            raise ValidationError("Title is required")

        user_subscription = UserSubscriptionSelector().get(user.pk)

        project = Project(
            title=title,
            limit_storage=user_subscription.product.max_project_storage,
            user=user
        )

        project.save()
        return project

    def update(self, data: Dict, project: Project) -> Project:
        title = data.get("title", None)

        if not title:
            raise ValidationError("Title is required")

        project.title = title
        project.save()
        return project

    def delete(self, project: Project) -> None:
        project.delete()
