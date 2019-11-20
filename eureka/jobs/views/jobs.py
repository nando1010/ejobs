"""Jobs views."""

#Django
from datetime import datetime, timedelta

# Django REST Framework
from rest_framework import mixins, viewsets,status
from rest_framework.response import Response

#Permissions
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from eureka.jobs.permissions.jobs import IsJobOwner
from eureka.utils.permissions.maintenance import IsRecruiterUser, IsStaffUser

#Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from eureka.jobs.serializers import JobModelSerializer, CreateJobSerializer,UpdateJobSerializer
from eureka.users.serializers import UserModelSerializer, ProfileModelSerializer

# Models
from eureka.jobs.models import Job
from eureka.users.models import User,Profile

#Utils
from django.utils import timezone

class JobViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Job view set."""

    serializer_class = JobModelSerializer
    lookup_field ='id'


    #Filters
    filter_backends = (SearchFilter,OrderingFilter,DjangoFilterBackend)
    SearchFilter_fields = ('company_ruc','company_name','title','description')
    OrderingFilter_fields = ('title','company_name')
    ordering = ('created')
    filter_fields=('is_verified','is_active')

    def get_permissions(self):
        """Asign permissions based on action."""
        permissions=[IsAuthenticatedOrReadOnly]
        if self.action in ['list','retrieve']:
            pass
        elif self.action in ['update','partial_update','destroy']:
            permissions.append(IsJobOwner)
            permissions.append(IsAuthenticated)
            permissions.append(IsRecruiterUser)
        elif self.action in ['create']:
            permissions.append(IsRecruiterUser)
        else:
            permissions.append(IsStaffUser)

        return[permission() for permission in permissions]


    def get_serializer_class(self):
        """Return serializer based on action."""
        if self.action == 'create':
            return CreateJobSerializer
        if self.action == 'update':
            return UpdateJobSerializer
        return JobModelSerializer
    #
    # def get_serializer_context(self):
    #     """Add job to serializer context."""
    #     context = super(JobViewSet,self).get_serializer_context
    #     context['job']=self.job

    def update(self,request,*args,**kwargs):
        response = super(JobViewSet, self).update(request, *args, **kwargs)
        return response


    def get_queryset(self):
        """Return active job"""
        queryset=Job.objects.all()
        now= timezone.now()
        if self.action == 'list':
            return queryset.filter(is_public=True,is_active=True,finished_at__gte=now)
        return queryset

    def create(self,request,*args,**kwargs):
        """Create job."""

        serializer = CreateJobSerializer(
            data = request.data,
            context = {'request': request}
        )
        serializer.is_valid(raise_exception = True)
        job = serializer.save()
        data = JobModelSerializer(job).data
        return Response(data, status=status.HTTP_201_CREATED)


    def retrieve(self,request,*args,**kwargs):
        """Add extra data to the response."""
        response = super(JobViewSet, self).retrieve(request, *args, **kwargs)
        user_id=self.request.user.id
        users=User.objects.filter(id=user_id)

        data = {
            'job':response.data,
            'user': UserModelSerializer(users,many = True).data
        }
        response.data = data
        return response
