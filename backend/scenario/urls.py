from django.urls import path

from .views import (
    ProjectListCreateAPIView,
    ProjectDetailDeleteUpdateAPIView,
    ScenarioCreateAPIView,
    ScenarioDetailDeleteAPIView,
    ScenarioHasRootAPIView,
    ScenarioTreeAPIView
)

urlpatterns_project = [
    path("project/", ProjectListCreateAPIView.as_view(), name="project_list_create"),
    path("project/<int:pk>/", ProjectDetailDeleteUpdateAPIView.as_view(), name="project_detail_update_delete"),
]

urlpatterns_scenario = [
    path("scenario/", ScenarioCreateAPIView.as_view(), name="scenario_create"),
    path("scenario/tree/<str:project_slug>/", ScenarioTreeAPIView.as_view(), name="scenario_tree"),
    path("scenario/<int:pk>/", ScenarioDetailDeleteAPIView.as_view(), name="scenario_delete_detail"),
    path("scenario/<int:project_id>/root/", ScenarioHasRootAPIView.as_view(), name="scenario_has_root"),
]

urlpatterns = urlpatterns_project + urlpatterns_scenario
