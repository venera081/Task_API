from django.urls import path
from .views import RegistrationAPIView, ConfirmEmailAPIView, AuthenticationAPIView, ResendConfirmationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from apps.users.google_oauth import GoogleLoginAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('confirm-email/<uuid:token>/', ConfirmEmailAPIView.as_view()),
    path('resend-confirmation/', ResendConfirmationAPIView.as_view()),
    path('authenticate/', AuthenticationAPIView.as_view()),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('google-login/', GoogleLoginAPIView.as_view()), 
]
