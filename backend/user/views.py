from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .repository.user import UserAccountRepository
from .services.user import UserAccountService


class UserRegisterAPIView(APIView):
    permission_classes = (AllowAny, )
    _service = UserAccountService(UserAccountRepository())

    def post(self, request):
        user = self._service.create(request=request)
        return Response(user, status=status.HTTP_201_CREATED)


class UserAccountMeAPI(APIView):
    permission_classes = (IsAuthenticated, )
    _service = UserAccountService(UserAccountRepository())

    def get(self, request):
        user = self._service.get(user_id=request.user.id)
        return Response(user, status=status.HTTP_200_OK)

    def put(self, request):
        user = self._service.update(user_id=request.user.id, request=request)
        return Response(user, status=status.HTTP_200_OK)
