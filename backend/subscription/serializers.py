from .models import Product, ProductPrice, UserSubscription
from rest_framework.serializers import ModelSerializer


class OutputProductPriceSerializer(ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ("id", "value", "currency")


class OutputProductSerializer(ModelSerializer):
    price = OutputProductPriceSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "max_project_storage", "num_of_projects")


class OutputUserSubscription(ModelSerializer):
    product = OutputProductSerializer()

    class Meta:
        model = UserSubscription
        fields = ("user", "product",  "is_active", "expiration_date")
