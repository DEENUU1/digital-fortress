from user.models import UserAccount
import pytest


@pytest.fixture()
def user_active() -> UserAccount:
    return UserAccount.objects.create_user(
        first_name="John",
        last_name="Doe",
        email="example@x.com",
        is_active=True,
    )
