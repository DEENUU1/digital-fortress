from typing import Any, Optional, List, Dict
from rest_framework.exceptions import NotFound
from user.models import UserAccount


class CRUDRepository:

    def __init__(self, model, user: UserAccount = None):
        self._model = model
        self._user = user

    def get_all(self) -> List[Optional[Any]]:
        if self._user:
            return self._model.objects.filter(user=self._user)
        else:
            return self._model.objects.all()

    def get_by_id(self, _id: int) -> Optional[Any]:
        if not self.exists(_id):
            raise NotFound(f"Object with id {_id} does not exist")

        if self._user:
            return self._model.objects.get(id=_id, user=self._user)
        else:
            return self._model.objects.get(id=_id)

    def create(self, data: Dict) -> Any:
        return self._model.objects.create(**data)

    def update(self, _id: int, data: Dict) -> Optional[Any]:
        if not self.exists(_id):
            raise NotFound(f"Object with id {_id} does not exist")

        obj = self.get_by_id(_id)

        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, _id: int) -> None:
        if not self.exists(_id):
            raise NotFound(f"Object with id {_id} does not exist")
        obj = self.get_by_id(_id)
        if obj:
            obj.delete()
            return None
        return None

    def exists(self, _id: int) -> bool:
        if self._user:
            return self._model.objects.filter(id=_id, user=self._user).exists()
        else:
            return self._model.objects.filter(id=_id).exists()
