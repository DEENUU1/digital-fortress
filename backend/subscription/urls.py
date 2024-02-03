from django.urls import path
from .views import ProductListView


urlpatterns_product = [
    path('/', ProductListView.as_view(), name='product_list'),
    # path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),

]

urlpatterns_subscription = [

]

urlpatterns = urlpatterns_product + urlpatterns_subscription
