from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .services import user_subscription as user_subscription_service, product as product_service
from .repository import user_subscription as user_subscription_repo, product as product_repo
from .serializers import OutputProductSerializer


class ProductListView(APIView):
    permission_classes = (AllowAny, )
    _service = product_service.ProductService(product_repo.ProductRepository())

    def get(self, request):
        instance = self._service.get_all()
        return Response(OutputProductSerializer(instance, many=True).data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    permission_classes = (AllowAny,)
    _service = product_service.ProductService(product_repo.ProductRepository())

    def get(self, request, product_id: int):
        instance = self._service.get_by_id(product_id)
        return Response(OutputProductSerializer(instance).data, status=status.HTTP_200_OK)


class UserSubscriptionGetView(APIView):
    permission_classes = (IsAuthenticated,)
    _service = user_subscription_service.UserSubscriptionService(user_subscription_repo.UserSubscriptionRepository())

    def get(self, request):
        instance = self._service.get_user_subscription(request.user.id)
        return Response(OutputProductSerializer(instance).data, status=status.HTTP_200_OK)
