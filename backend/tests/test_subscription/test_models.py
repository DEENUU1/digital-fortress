import pytest
from .fixtures import product_price, product, user_subscription


@pytest.mark.django_db
def test_product_price_create_object_success(product_price):
    assert product_price.value == 10
    assert product_price.currency == "USD"
    assert product_price.created_at
    assert product_price.updated_at


@pytest.mark.django_db
def test_product_create_object_success(product):
    assert product.name == "testproduct"
    assert product.created_at
    assert product.updated_at
    assert product.max_project_storage == 300
    assert product.num_of_projects == 3


@pytest.mark.django_db
def test_user_subscription_create_object_success(user_subscription):
    assert user_subscription.created_at
    assert user_subscription.updated_at
    assert user_subscription.user == user_subscription.user
    assert str(user_subscription) == str("example3@x.com testproduct")
