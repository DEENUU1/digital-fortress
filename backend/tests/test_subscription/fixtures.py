from datetime import datetime, timedelta

import pytest

from subscription.models import Product, ProductPrice, UserSubscription
from user.models import UserAccount


@pytest.fixture()
def product_price() -> ProductPrice:
    return ProductPrice.objects.create(
        value=10,
        currency="USD",
        price_id="testpriceid123"
    )


@pytest.fixture()
def product(product_price) -> Product:
    product_instance = Product.objects.create(
        name="testproduct",
        description="short description of a product",
        max_project_storage=300,
        num_of_projects=3,
        is_active=True,
    )
    product_instance.price.set([product_price])
    return product_instance


@pytest.fixture()
def user_subscription(product) -> UserSubscription:
    user = UserAccount.objects.create_user(
        first_name="John",
        last_name="Doe",
        email="example3@x.com",
        is_active=True,
    )

    return UserSubscription(
        user=user,
        product=product,
        is_active=True,
        expiration_date=datetime.now() + timedelta(days=30)
    )
