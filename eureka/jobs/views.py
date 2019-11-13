"""Job views."""

#Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from eureka.jobs.models import Job

#Serializer
from eureka.jobs.serializer import JobSerializer, CreateJobSerializer

@api_view(['GET'])
def list_jobs(request):
    """List jobs."""
    jobs = Job.objects.filter(is_active = True)
    serializer = JobSerializer(jobs,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_job(request):
    """Create job."""
    serializer = CreateJobSerializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    job = serializer.save()
    return Response(JobSerializer(job).data)
