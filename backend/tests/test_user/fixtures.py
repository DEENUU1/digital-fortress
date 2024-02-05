from user.models import UserAccount
import pytest


@pytest.fixture()
def user_active() -> UserAccount:
    user = UserAccount.objects.create_user(
        first_name="John",
        last_name="Doe",
        email="example@x.com",
        is_active=True,
    )
    user.save()
    return user


@pytest.fixture()
def user_two() -> UserAccount:
    user = UserAccount.objects.create_user(
        first_name="John111",
        last_name="Doe111",
        email="example1111@x.com",
        is_active=True,
    )
    user.save()
    return user


@pytest.fixture()
def user_inactive() -> UserAccount:
    return UserAccount.objects.create_user(
        first_name="John",
        last_name="Doe",
        email="example2@x.com",
        is_active=False,
    )
