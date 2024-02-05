from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository.user import UserAccountRepository
from .services.user import UserAccountService


class UserAccountMeAPI(APIView):
    permission_classes = [IsAuthenticated]
    user_service = UserAccountService(UserAccountRepository())

    def get(self, request):
        user = self.user_service.get(user_id=request.user.id)
        return Response(user, status=status.HTTP_200_OK)

    def put(self, request):
        user = self.user_service.update(user_id=request.user.id, data=request.data)
        return Response(user, status=status.HTTP_200_OK)
