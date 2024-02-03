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


@pytest.fixture()
def user_inactive() -> UserAccount:
    return UserAccount.objects.create_user(
        first_name="John",
        last_name="Doe",
        email="example2@x.com",
        is_active=False,
    )
