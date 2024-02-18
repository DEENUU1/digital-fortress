from django.db import models
from utils.model_base import BaseModel
from user.models import UserAccount


class File(BaseModel):
    STATUS = (
        ("Uploaded", "Uploaded"),
        ("Processing", "Processing"),
        ("Processed", "Processed"),
    )

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="Uploaded")
    file = models.FileField(upload_to="files/")

    def __str__(self) -> str:
        return f"{self.user} {self.status}"
