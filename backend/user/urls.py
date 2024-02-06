from django.urls import path
from .views import (
    UserAccountMeAPI,
    UserRegisterAPIView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)

urlpatterns_jwt = [
    path('token/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('token/logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns_user = [
    path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),
    path('register/', UserRegisterAPIView.as_view(), name="register")
]


urlpatterns = urlpatterns_jwt + urlpatterns_user
