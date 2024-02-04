from django.db import models
from utils.model_base import BaseModel
from user.models import UserAccount


class Project(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    limit_storage = models.IntegerField(default=0)
    current_storage = models.IntegerField(default=0)
    num_of_scenarios = models.IntegerField(default=0)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    @property
    def storage_usage(self):
        return f"{self.current_storage}/{self.limit_storage}"
