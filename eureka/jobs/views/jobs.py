"""Jobs views."""

# Django REST Framework
from rest_framework import mixins, viewsets,status
from rest_framework.response import Response

#Permissions
from rest_framework.permissions import IsAuthenticated
from eureka.jobs.permissions.jobs import IsJobOwner

# Serializers
from eureka.jobs.serializers import JobModelSerializer, CreateJobSerializer
from eureka.users.serializers import UserModelSerializer, ProfileModelSerializer

# Models
from eureka.jobs.models import Job
from eureka.users.models import User,Profile

class JobViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Job view set."""

    serializer_class = JobModelSerializer
    lookup_field ='id'

    def get_permissions(self):
        """Asign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['update','partial_update','destroy']:
            permissions.append(IsJobOwner)
        return[permission() for permission in permissions]


    # def get_serializer_class(self):
    #     """Return serializer based on action."""
    #     if self.action == 'create':
    #         return CreateJobSerializer
    #     return JobModelSerializer
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
        if self.action == 'list':
            return queryset.filter(is_public=True,is_active=True)
        return queryset

    def create(self,request,*args,**kwargs):
        """Create job."""
        data=request.data
        data['user']=self.request.user.id
        data['profile']=self.request.user.profile.id
        serializer = CreateJobSerializer(data=data)
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
