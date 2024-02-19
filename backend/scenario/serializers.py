from rest_framework.serializers import ModelSerializer

from .models import Project, Scenario


class InputProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "user")


class OutputProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "limit_storage",
            "current_storage",
            "num_of_scenarios",
            "user",
            "created_at",
            "updated_at",
            "storage_usage",
            "storage_percentage"
        )


class InputScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = ("parent_id", "project", "user_details", "user")


class OutputScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = (
            "id",
            "parent_id",
            "response",
            "project",
            "user_details",
            "user",
            "created_at",
            "updated_at",
        )
