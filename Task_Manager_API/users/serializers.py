from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError({"password": "Passwords do not match"})

        validate_password(data['password'])
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False   
        )
        return user
    
class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_active:
            raise serializers.ValidationError(
                "User account is not activated yet!"
            )

        return data

class ResendConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
    
        authenticate_kwargs = {
            'email': attrs['email'],
            'password': attrs['password'],
        }
        self.user = authenticate(**authenticate_kwargs)
        if not self.user or not self.user.is_active:
            raise serializers.ValidationError(
                'No active account found with the given credentials'
            )
        data = super().validate(attrs)
        return data



