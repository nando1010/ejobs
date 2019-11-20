"""Users Serializers."""

# Django
from django.conf import settings
from django.contrib.auth import authenticate, password_validation
from django.core.mail import EmailMultiAlternatives
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#Serializers
from eureka.users.serializers.profiles import ProfileModelSerializer

# Models
from eureka.users.models import User,Profile

# Tasks
from eureka.taskapp.tasks import send_confirmation_email

# Utilities
import jwt
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    profile = ProfileModelSerializer(read_only = True)

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'profile',
            'jobs_created',
            'jobs_applied'
        )


class UserSignUpSerializer(serializers.Serializer):
    """User Sign Up serializer.

    Handdle the sign up data validation and puser/profile creation
    """

    email = serializers.EmailField(
        validators =[
            UniqueValidator(queryset = User.objects.all())
        ]
    )

    # First name
    first_name = serializers.CharField(
        min_length = 2,
        max_length = 30
    )

    last_name = serializers.CharField(
        min_length = 2,
        max_length=150
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in the format: +99999999. Up to 15 digits are allowed"
    )
    phone_number = serializers.CharField(
        required = False,
        allow_blank = True
    )

    # Password
    password = serializers.CharField(
        min_length=8
    )
    password_confirmation = serializers.CharField(
        min_length = 8
    )

    def validate(self,data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError('Las contraseñas no coinciden.')
        password_validation.validate_password(passwd)
        return data

    def create(self,data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(**data,is_verified=False, is_client = True)
        profile = Profile.objects.create(user = user)
        send_confirmation_email.delay(user_pk=user.pk)
        return user

class UserLoginSerializer(serializers.Serializer):
    """User Login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length = 8)

    def validate(self,data):
        """Check credentials."""
        user = authenticate(username=data['email'],password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Tu cuenta aun no esta activa:')
        self.context['user'] = user
        return data

    def create(self,data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'],token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account Verification serializer."""

    token = serializers.CharField()

    def validate_token(self,data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data,settings.SECRET_KEY,algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('Invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializer.ValidationError('Invalid token')

        self.context['payload']=payload
        return data

    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(email=payload['user'])
        user.is_verified=True
        user.save()
