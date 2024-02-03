from ..models import UserAccount


class UserAccountSelector:

    def __init__(self, user: UserAccount):
        self.user = user

    def get_me(self) -> UserAccount:
        return self.user
