from django.urls import path
# from .views import UserAccountMeAPI


urlpatterns_product = [
    # path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),

]

urlpatterns_subscription = [

]

urlpatterns = urlpatterns_product + urlpatterns_subscription
