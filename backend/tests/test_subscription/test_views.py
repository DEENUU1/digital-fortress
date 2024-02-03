from .fixtures import product_price, product, user_subscription
import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from subscription.views import ProductDetailView, ProductListView, UserSubscriptionGetView


factory = APIRequestFactory()


@pytest.mark.django_db
def test_product_list_view_success(product_price, product) -> None:
    request = factory.get("api/v1/subscription/")
    view = ProductListView.as_view()

    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail_success(product, product_price) -> None:
    request = factory.get("api/v1/subscription/1/")
    view = ProductDetailView.as_view()

    response = view(request, product_id=1)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail_invalid_product_id_error(product, product_price) -> None:
    request = factory.get("api/v1/subscription/1/")
    view = ProductDetailView.as_view()

    response = view(request, product_id=3)

    assert response.status_code == 404


@pytest.mark.django_db
def test_user_subscription_get_authenticated_success(user_subscription, product_price) -> None:
    request = factory.get("api/v1/subscription/me")
    view = UserSubscriptionGetView.as_view()
    force_authenticate(request, user=user_subscription.user)
    response = view(request)

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_subscription_get_unauthenticated_success(user_subscription, product_price) -> None:
    request = factory.get("api/v1/subscription/me")
    view = UserSubscriptionGetView.as_view()
    response = view(request)

    assert response.status_code == 401
