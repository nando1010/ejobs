"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator

# Utilities
from eureka.utils.models import EurekaModel

class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        """
        Internal Method for Creating and saving a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email=self.normalize_email(email)
        user = self.model(
            email=email,
            password = password,
            first_name = first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.is_verified=False
        user.save()
        return user

    def create_user(self, email, password, first_name, last_name,phone_number,**extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        user = self._create_user(email=email, password=password,first_name=first_name,last_name=last_name,**extra_fields)
        user.phone_number=phone_number
        user.is_staff= False
        user.is_superuser=False
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name,**extra_fields):
        """
        Creates and saves a SuperUser with the given email and password.
        """
        user = self._create_user(email=email, password=password,first_name=first_name,last_name=last_name,**extra_fields)
        user.is_staff= True
        user.is_superuser=True
        user.is_verified=True
        user.save()
        return user


    def get_by_natural_key(self,email_):
        print(email_)
        return self.get(email=email_)

class User(EurekaModel,AbstractBaseUser,PermissionsMixin):
    """User model.
    Here we are subclassing the Django AbstractBaseUser, which comes with only
    3 fields:
    1 - password
    2 - last_login
    3 - is_active
    Note than all fields would be required unless specified otherwise, with
    `required=False` in the parentheses.

    The PermissionsMixin is a model that helps you implement permission settings
    as-is or modified to your requirements.
    More info: https://goo.gl/YNL2ax
    """

    email = models.EmailField(
        'email address',
        unique = True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    first_name = models.CharField(
        max_length=30,
        verbose_name='first name'
    )

    last_name=models.CharField(
        max_length=150,
        verbose_name='last name'
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

    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this admin site.',
        verbose_name='staff status'
    )

    is_superuser = models.BooleanField(
        default=False,
        help_text='Designates whether the user can have superuser attributes.',
        verbose_name='superuser status'
    )

    is_client = models.BooleanField(
        'client',
        default = True,
        help_text=(
            'Help easly distinguish users and perfom queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default = False,
        help_text = 'Set to true when the user has verified its email adress.'
    )

    is_active= models.BooleanField(
        'active',
        default = True,
        help_text = 'Set to true when the user has an active account.'
    )

    def __get_short_name(self):
        """Return email."""
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        """Return email."""
        return self.email
