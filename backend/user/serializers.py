from rest_framework.serializers import ModelSerializer
from .models import UserAccount


class OutputUserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "openai_key",
        )


class InputUpdateUserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "first_name",
            "last_name",
            "openai_key"
        )


class InputCreateUserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
        )


class InputAPIKey(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            "openai_key",
        )