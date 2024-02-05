from django.urls import path

from .views import (
    ProjectManagementAPIView,
    ProjectDetailsAPIView,
    ScenarioDetailsAPIView,
    ScenarioManagementAPIView,
    ScenarioHasRootAPIView
)

urlpatterns_project = [
    path("project/", ProjectManagementAPIView.as_view(), name="project_management"),
    path("project/<str:project_slug>/", ProjectDetailsAPIView.as_view(), name="project_details"),
]

urlpatterns_scenario = [
    path("scenario/", ScenarioManagementAPIView.as_view(), name="scenario_management"),
    path("scenario/<int:scenario_id>/", ScenarioDetailsAPIView.as_view(), name="scenario_details"),
    path("scenario/<int:scenario_id>/root/", ScenarioHasRootAPIView.as_view(), name="scenario_has_root"),
]

urlpatterns = urlpatterns_project + urlpatterns_scenario
