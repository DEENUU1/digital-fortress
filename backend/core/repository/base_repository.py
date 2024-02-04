from typing import Any, Optional, List, Dict
from django.db import models


class CRUDRepository:

    def __init__(self, model: models.Model):
        self._model = model

    def get_all(self) -> List[Optional[Any]]:
        return self._model.objects.all()

    def get_by_id(self, _id: int) -> Optional[Any]:
        try:
            return self._model.objects.get(id=_id)
        except self._model.DoesNotExist:
            return None

    def create(self, data: Dict) -> Any:
        return self._model.objects.create(**data)

    def update(self, _id: int, data: Dict) -> Optional[Any]:
        obj = self.get_by_id(_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, _id: int) -> None:
        obj = self.get_by_id(_id)
        if obj:
            obj.delete()
            return None

    def exists(self, _id: int) -> bool:
        return self._model.objects.filter(id=_id).exists()
