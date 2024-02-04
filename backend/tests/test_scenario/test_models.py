import pytest

from tests.test_user.fixtures import user_active
from .fixture import project, scenario_root, scenario_children


@pytest.mark.django_db
def test_create_project_object_success(project) -> None:
    assert project.title == "Test Project"
    assert project.limit_storage == 300
    assert project.current_storage == 100
    assert project.num_of_scenarios == 10
    assert project.storage_usage == "100/300"


@pytest.mark.django_db
def test_create_scenario_root_object_success(project, user_active, scenario_root) -> None:
    assert scenario_root.project == project
    assert scenario_root.response == "Hey I am AI assistant"


@pytest.mark.django_db
def test_create_scenario_children_object_success(project, user_active, scenario_children, scenario_root) -> None:
    assert scenario_children.project == project
    assert scenario_children.response == "How can i help you?"
    assert scenario_root.project_id == 1
