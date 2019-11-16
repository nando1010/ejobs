"""Users views."""

# Django REST framework
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from eureka.users.serializers import (
    UserLoginSerializer,
    UserSignUpSerializer,
    UserModelSerializer,
    AccountVerificationSerializer
)

class UserViewSet(viewsets.GenericViewSet):
    """User view set.

    # Handle sign up, login and account verification.
    # """

    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'])
    def login(self,request):
        """User log in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED )


    @action(detail=False,methods=['post'])
    def signup(self,request):
        """User sign up."""
        permissions = [AllowAny]
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED )

    @action(detail=False,methods=['post'])
    def verify(self,request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        data = {'message':'Felicitaciones , ahora puedes encontrar las mejores ofertas laborales!'}
        return Response(data, status=status.HTTP_200_OK)
