from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from .serializers import RegistrationSerializer, AuthTokenObtainPairSerializer, ResendConfirmationSerializer, CustomTokenObtainPairSerializer
from .models import EmailConfirmation
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()



class RegistrationAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        confirmation = EmailConfirmation.objects.create(user=user)
        confirm_link = f"http://127.0.0.1:8000/api/v1/users/confirm-email/{confirmation.token}/"
        send_mail(
            subject="Confirm your email",
            message=f"Click to confirm: {confirm_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return Response(
            {"detail": "Confirmation email sent"},
            status=status.HTTP_201_CREATED
        )

class AuthenticationAPIView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer

    
    
class ConfirmEmailAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, token):
        confirmation = get_object_or_404(EmailConfirmation, token=token)
        user = confirmation.user
        if confirmation.created_at + timedelta(hours=24) < timezone.now():
            confirmation.delete()
            return Response(
                {"detail": "Confirmation link expired"},
                status=400
            )

        user.is_active = True
        user.save()
        confirmation.delete()
        return Response(
            {"message": "Email successfully confirmed"},
            status=status.HTTP_200_OK
        )
    
       

class ResendConfirmationAPIView(GenericAPIView):
    serializer_class = ResendConfirmationSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = get_object_or_404(User, email=email)

        if user.is_active:
            return Response(
                {"detail": "Email already confirmed"},
                status=status.HTTP_400_BAD_REQUEST
            )
        EmailConfirmation.objects.filter(user=user).delete()
        confirmation = EmailConfirmation.objects.create(user=user)
        confirm_link = f"http://127.0.0.1:8000/api/v1/users/confirm-email/{confirmation.token}/"
        send_mail(
            subject="Confirm your email",
            message=f"Click to confirm: {confirm_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return Response(
            {"detail": "Confirmation email resent"},
            status=status.HTTP_200_OK
        )
    
class CustomObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
