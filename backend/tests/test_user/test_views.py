from .fixtures import user_active
import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from user.views import UserAccountMeAPI
from user.models import UserAccount


factory = APIRequestFactory()


@pytest.mark.django_db
def test_user_account_me_get_authenticated_success(user_active: UserAccount) -> None:
    request = factory.get('api/v1/user/me')
    view = UserAccountMeAPI.as_view()

    force_authenticate(request, user=user_active)
    response = view(request)

    assert response.status_code == 200
    assert response.data == {
        "id": 1,
        "first_name": user_active.first_name,
        "last_name": user_active.last_name,
        "email": user_active.email,
    }
