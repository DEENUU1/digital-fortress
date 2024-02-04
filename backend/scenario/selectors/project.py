from typing import Dict

from rest_framework.exceptions import ValidationError

from scenario.models import Project, Scenario
from subscription.selectors.user_subscription import UserSubscriptionSelector
from user.models import UserAccount
from typing import List


class ProjectSelector:

    def list(self) -> List[Project]:
        return Project.objects.all()

    def get(self, project_slug: str) -> Project:
        return Project.objects.get(slug=project_slug)

    def has_root(self, project_slug: str) -> bool:
        return Scenario.objects.filter(project__slug=project_slug, parent_id=None).exists()
