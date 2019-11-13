"""Users views."""

# Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from eureka.users.serializers import (
    UserLoginSerializer,
    UserSignUpSerializer,
    UserModelSerializer
)


class UserLoginAPIView(APIView):
    """User login API View."""

    def post(self,request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED )


class UserSignUpAPIView(APIView):
    """User sign up API View."""

    def post(self,request, *args, **kwargs):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED )
