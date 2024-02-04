from scenario.models import Project
from rest_framework.exceptions import ValidationError
from user.models import UserAccount
from typing import Dict
from subscription.selectors.user_subscription import UserSubscriptionSelector


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
