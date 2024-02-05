from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.urls import path
from .views import UserAccountMeAPI, UserRegisterAPIView


urlpatterns_jwt = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', TokenBlacklistView.as_view(), name='logout'),
]

urlpatterns_user = [
    path('me/', UserAccountMeAPI.as_view(), name='user_account_get_me'),
    path('register/', UserRegisterAPIView.as_view(), name="register")
]


urlpatterns = urlpatterns_jwt + urlpatterns_user
