from django.urls import path
from .views import ProductListView, ProductDetailView, UserSubscriptionGetView


urlpatterns_product = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name="product_details"),
]

urlpatterns_subscription = [
    path('me/', UserSubscriptionGetView.as_view(), name="user_subscription"),
]

urlpatterns = urlpatterns_product + urlpatterns_subscription
