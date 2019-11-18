"""Jobs views."""

# Django REST Framework
from rest_framework import mixins, viewsets

#Permissions
from rest_framework.permissions import IsAuthenticated
from eureka.jobs.permissions.jobs import IsJobOwner

# Serializers
from eureka.jobs.serializers import JobModelSerializer

# Models
from eureka.jobs.models import Job

class JobViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """Job view set."""

    serializer_class = JobModelSerializer
    lookup_field ='id'

    def get_queryset(self):
        """Restrict jobs to public and active-only."""
        queryset = Job.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True,is_active=True)
        return queryset

    def get_permissions(self):
        """Asign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['update','partial_update']:
            permissions.append(IsJobOwner)
        return[permission() for permission in permissions]

    def perform_create(self,serializer):
        """Assign job."""
        job = serializer.save()
        user = self.request.user
        # profile = user.profile
