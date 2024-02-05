from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import OutputProductSerializer
from .services.user_subscription import UserSubscriptionService
from .repository.user_subscription import UserSubscriptionRepository
from .services.product import ProductService
from .repository.product import ProductRepository


class ProductListView(APIView):
    permission_classes = (AllowAny, )
    _service = ProductService(ProductRepository())

    def get(self, request):
        products = self._service.get_all()
        serializer = OutputProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    permission_classes = (AllowAny,)
    _service = ProductService(ProductRepository())

    def get(self, request, product_id: int):
        product = self._service.get_by_id(product_id)
        serializer = OutputProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSubscriptionGetView(APIView):
    permission_classes = (IsAuthenticated,)
    _service = UserSubscriptionService(UserSubscriptionRepository())

    def get(self, request):
        product = self._service.get_user_subscription(request.user.id)
        serializer = OutputProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
