import requests
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from apps.users.serializers import OauthSerializer
from rest_framework.permissions import AllowAny
import os 

User = get_user_model()


class GoogleLoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = OauthSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"]

        token_response = requests.post(
            url="https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
                "client_secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
                "redirect_uri": os.environ.get("GOOGLE_CLIENT_URI"),
                "grant_type": "authorization_code"
            },
        )
        print("CLIENT ID:", os.environ.get("GOOGLE_CLIENT_ID"))
        print(os.environ.get("GOOGLE_CLIENT_SECRET"))
        print(os.environ.get("GOOGLE_CLIENT_URI"))



            
        # token_data = token_response.json()
        if token_response.status_code != 200:
            return Response(token_response.json(), status=400)
        access_token = token_data.get("access_token")

        if not access_token:
            return Response({"error": "Invalid access token!"}, status=400)
        
        user_info = requests.get(
            url="https://www.googleapis.com/oauth2/v3/userinfo",
            params={"alt": "json"},
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        print(f"user_info {user_info}")

        email = user_info['email']
        if not email:
            return Response({"error": "Email not provided"}, status=400)

        user, created = User.objects.get_or_create(email=email, defaults={
            "is_active": True,
            "registration_source": "google"
    })

        user.is_active = True
        # user.last_login = timezone.now()

        if created:
            user.registration_source = "google"
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({"access_token": str(refresh.access_token),
                        "refresh_token": str(refresh)})
        


