from django.urls import path
from .views import ProductListView, ProductDetailView, UserSubscriptionGetView


urlpatterns_product = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:product_id>/', ProductDetailView.as_view(), name="product_details"),
]

urlpatterns_subscription = [
    path('me/', UserSubscriptionGetView.as_view(), name="user_subscription"),
]

urlpatterns = urlpatterns_product + urlpatterns_subscription
