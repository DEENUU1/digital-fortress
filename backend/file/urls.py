from django.urls import path

from .views import (
    FileUploadAPIView,
    FileListAPIView,
)

urlpatterns_file = [
    path("", FileUploadAPIView.as_view(), name="file_upload"),
    path("<int:project_id>/", FileListAPIView.as_view(), name="file_list"),
]


urlpatterns = urlpatterns_file
