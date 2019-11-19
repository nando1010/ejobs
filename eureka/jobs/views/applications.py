"""Applications views."""

#Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#Permissions
from rest_framework.permissions import IsAuthenticated

#Serializers
from eureka.jobs.serializers import CreateApplicationSerializer,ApplicationModelSerializer

#Models
from eureka.jobs.models import Job,Application

class ApplicationViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):

    serializer_class=CreateApplicationSerializer
    permission_classes = [IsAuthenticated]

    def dispatch(self,request,*args,**kwargs):
        """Verify that the job exists."""
        job_id =kwargs['pk']
        self.job=get_object_or_404(Job,id=job_id)
        return super(ApplicationViewSet,self).dispatch(request,*args,**kwargs)

    def get_serializer_context(self):
        """Add job to serializer context."""
        context = super(ApplicationViewSet,self).get_serializer_context()
        context['job']=self.job

    def create(self,request,*args,**kwargs):

        serializer = CreateApplicationSerializer(
            data = request.data,
            context = {'job': self.job, 'request': request}
        )
        
        serializer.is_valid(raise_exception=True)

        application = serializer.save()

        data = ApplicationModelSerializer(application).data
        # ApplicationModelSerializer

        return Response(data, status=status.HTTP_201_CREATED)
