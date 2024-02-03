from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import UserAccountMeAPI


urlpatterns_jwt = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns_user = [
    path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),

]

urlpatterns = urlpatterns_jwt + urlpatterns_user
