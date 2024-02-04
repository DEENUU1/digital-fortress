import pytest
from scenario.models import Project, Scenario
from tests.test_user.fixtures import user_active


@pytest.fixture()
def project(user_active) -> Project:
    return Project.objects.create(
        title='Test Project',
        slug='test-project',
        limit_storage=300,
        current_storage=100,
        num_of_scenarios=10,
        user=user_active
    )


@pytest.fixture()
def scenario_root(project) -> Scenario:
    return Scenario.objects.create(
        project=project,
        response="Hey I am AI assistant",
        user_details="Hi, what's your name"
    )


@pytest.fixture()
def scenario_children(scenario_root, project) -> Scenario:
    return Scenario.objects.create(
        project_id=1,
        project=project,
        response="How can i help you?"
    )
