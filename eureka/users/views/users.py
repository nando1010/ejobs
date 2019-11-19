"""Users views."""

# Django REST framework
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated
)
from eureka.users.permissions import IsAccountOwner

from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from eureka.users.serializers import (
    UserLoginSerializer,
    UserSignUpSerializer,
    UserModelSerializer,
    AccountVerificationSerializer
)
from eureka.jobs.serializers import JobModelSerializer
from eureka.users.serializers.profiles import ProfileModelSerializer

#Models
from eureka.users.models import User
from eureka.jobs.models import Job

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    # Handle sign up, login and account verification.
    # """

    queryset = User.objects.filter(is_active = True, is_client = True)
    serializer_class = UserModelSerializer
    # PENDIENTE_EUREKA: Agregar el link de usuario
    # lookup_field = 'first_name'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup','login','verify']:
            permissions = [AllowAny]
        elif self.action in ['update','partial_update']:
            permissions= [IsAuthenticated,IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return[p() for p in permissions]

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

    @action(detail=True, methods=['put','patch'])
    def profile(self,request,*args,**kwargs):
        """Update profile data."""
        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial = partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)

    def retrieve(self,request,*args,**kwargs):
        """Add extra data to the response."""
        response = super(UserViewSet,self).retrieve(request, *args, **kwargs)

        jobs=Job.objects.filter(is_active=True)

        data = {
            'user':response.data,
            'jobs': JobModelSerializer(jobs,many = True).data
        }
        response.data = data
        return response
