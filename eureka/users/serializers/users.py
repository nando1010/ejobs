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

# Models
from eureka.users.models import User,Profile

# Utilities
import jwt
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'phone_number',
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
        user = User.objects.create_user(**data,is_verified=False)
        profile = Profile.objects.create(user = user)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self,user):
        """Send account verification link to given user."""
        verification_token = self.gen_verification_token(user)
        subject = 'Welcome @{}! Verify your account to start using Eureka Jobs'.format(user.first_name)
        from_email = 'Eureka Jobs <noreply@eureka.com>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {
            'token': verification_token,
            'user':user
            }
        )
        msg = EmailMultiAlternatives(subject,content,from_email,[user.email])
        msg.attach_alternative(content,"text/html")
        msg.send()

    def gen_verification_token(self,user):
        """Create JWT token that the user can use to verify its account."""
        exp_date = timezone.now() + timedelta(days = 1)
        payload = {
            'user': user.email,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm = 'HS256')
        return token.decode()


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
