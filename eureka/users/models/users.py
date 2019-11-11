"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager

# Utilities
from eureka.utils.models import EurekaModel

class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(EurekaModel,AbstractUser):
    """User model.

    Extend from Django's AbstractUser, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique = True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in the format: +99999999. Up to 15 digits are allowed"
    )
    phone_number = models.CharField(
        'phone number',
        validators=[phone_regex],
        max_length = 17,
        blank = True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    objects = MyUserManager()

    is_client = models.BooleanField(
        'client',
        default = True,
        help_text=(
            'Help easly distinguish users and perfom queries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default = True,
        help_text = 'Set to true when the user have verified its email adress.'
    )

    def __str__(self):
        """Return email."""
        return self.email

    def __get_short_name(self):
        """Return email."""
        return self.email
