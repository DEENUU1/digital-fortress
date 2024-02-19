from django.urls import path

from .views import (
    FileUploadAPIView,
)

urlpatterns_file = [
    path("", FileUploadAPIView.as_view(), name="file_upload"),
]


urlpatterns = urlpatterns_file
