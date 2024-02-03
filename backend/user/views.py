from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .selectors.user import UserAccountSelector
from .serializers import OutputUserAccountSerializer
from .services.user import UserAccountService


class UserAccountMeGetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserAccountSelector(request.user).get_me()
        return Response(OutputUserAccountSerializer(user).data, status=status.HTTP_200_OK)


class UpdateUserAccountAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        UserAccountService(request.user).update(request.data)
        return Response("Account updated", status=status.HTTP_200_OK)
