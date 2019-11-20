#Django REST Framework
from rest_framework import mixins, viewsets

#Permissions
from rest_framework.permissions import IsAuthenticated
from eureka.utils.permissions.maintenance import IsStaffUser

#Serializers
from eureka.companies.serializers import CompanyModelSerializer
from eureka.jobs.serializers import JobModelSerializer

#Models
from eureka.companies.models import Company
from eureka.jobs.models import Job


class CompanyViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Company ViewSet."""

    serializer_class = CompanyModelSerializer
    lookup_field='ruc'

    def get_queryset(self):
        """ list to public-only."""
        queryset = Company.objects.filter(is_active= True)
        return queryset

    def perform_create(self,serializer):
        """Create company sector."""
        company=serializer.save()

    def get_permissions(self):
        """Asign permissions based on action."""
        permissions=[]
        if self.action in ['create','update','partial_update','destroy']:
            permissions.append(IsAuthenticated)
            permissions.append(IsStaffUser)
        if self.action in ['list','retrieve']:
            pass
        else:
            permissions.append(IsAuthenticated)
            permissions.append(IsStaffUser)
        return[permission() for permission in permissions]

    def retrieve(self,request,*args,**kwargs):
        """Add extra data to the response."""
        response = super(CompanyViewSet,self).retrieve(request, *args, **kwargs)
        company_ruc =kwargs['ruc']
        jobs=Job.objects.filter(
            is_active=True,
            company_ruc=company_ruc
        )

        data = {
            'company':response.data,
            'jobs': JobModelSerializer(jobs,many = True).data
        }
        response.data = data
        return response

    def update(self,request,*args,**kwargs):
        response = super(CompanyViewSet, self).update(request, *args, **kwargs)
        return response
