import pytest
from .fixtures import user_active
from user.models import UserAccount


@pytest.mark.django_db
def test_create_user_account_object(user_active: UserAccount) -> None:
    assert str(user_active) == user_active.email
    assert user_active.is_active
    assert user_active.is_staff is False
    assert user_active.first_name == "John"
