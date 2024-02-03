from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .selectors.product import ProductSelector
from .serializers import OutputProductPriceSerializer, OutputProductSerializer, OutputUserSubscription


class ProductListView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        products = ProductSelector().list()
        serializer = OutputProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
