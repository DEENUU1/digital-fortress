from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from selectors.user import UserAccountSelector


class UserAccountMeGetAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserAccountSelector.get_me(request.user.id)
        return Response(user, status=status.HTTP_200_OK)
