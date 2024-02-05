from rest_framework.serializers import ModelSerializer
from .models import Project, Scenario


class InputProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title")


class OutputProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "slug", "limit_storage", "current_storage", "num_of_scenarios", "user")


class InputScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = ("parent_id", "project", "user_details")


class OutputScenarioSerializer(ModelSerializer):
    class Meta:
        model = Scenario
        fields = ("parent_id", "response", "user_details", "user")
