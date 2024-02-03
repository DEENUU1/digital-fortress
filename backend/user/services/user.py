from ..models import UserAccount
from typing import Optional, Dict


class UserAccountService:

    def __init__(self, user: UserAccount):
        self.user = user

    def update(self, data: Dict[str, str]) -> None:
        first_name = data.get("first_name", None)
        last_name = data.get("last_name", None)

        if not first_name or not last_name:
            raise ValueError("First name or last name can not be none")

        self.user.first_name = first_name
        self.user.last_name = last_name
        self.user.save()
