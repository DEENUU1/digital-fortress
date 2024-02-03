from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .selectors.product import ProductSelector
from .selectors.user_subscription import UserSubscriptionSelector
from .serializers import OutputProductSerializer, OutputUserSubscription


class ProductListView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        products = ProductSelector().list()
        serializer = OutputProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, product_id: int):
        product = ProductSelector().get(product_id)
        serializer = OutputProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSubscriptionGetView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_subscription = UserSubscriptionSelector().get(request.user.id)
        serializer = OutputUserSubscription(user_subscription)
        return Response(serializer.data, status=status.HTTP_200_OK)
