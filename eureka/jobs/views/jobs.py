"""Jobs views."""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from eureka.jobs.serializers import JobModelSerializer

# Models
from eureka.jobs.models import Job

class JobViewSet(viewsets.ModelViewSet):
    """Job view set."""

    queryset = Job.objects.all()
    serializer_class = JobModelSerializer
