from django.urls import path
from .views import (
    UserAccountMeAPI,
    UserRegisterAPIView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    UpdateOpenAIAPIKeyAPI
)

urlpatterns_jwt = [
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns_user = [
    path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),
    path('register/', UserRegisterAPIView.as_view(), name="register"),
    path('me/api_key/', UpdateOpenAIAPIKeyAPI.as_view(), name="update_api_key"),
]


urlpatterns = urlpatterns_jwt + urlpatterns_user
