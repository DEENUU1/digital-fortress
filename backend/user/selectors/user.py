from ..models import UserAccount
from ..serializers import OutputUserAccountSerializer


class UserAccountSelector:

    def __init__(self, user: UserAccount):
        self.user = user

    def get_me(self) -> OutputUserAccountSerializer:
        return OutputUserAccountSerializer(self.user)
