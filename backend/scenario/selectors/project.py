from typing import Dict

from rest_framework.exceptions import ValidationError

from scenario.models import Project
from subscription.selectors.user_subscription import UserSubscriptionSelector
from user.models import UserAccount
from typing import List


class ProjectSelector:

    def list(self) -> List[Project]:
        return Project.objects.all()

    def get(self, project_slug: str) -> Project:
        return Project.objects.get(slug=project_slug)
