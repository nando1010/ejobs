#Django REST Framework
from rest_framework import mixins, viewsets

#Permissions
from rest_framework.permissions import IsAuthenticated
from eureka.utils.permissions.maintenance import IsStaffUser

#Serializers
from eureka.companies.serializers import CompanyModelSerializer

#Models
from eureka.companies.models import Company


class CompanyViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Company ViewSet."""

    serializer_class = CompanyModelSerializer

    permission_classes = [IsAuthenticated,IsStaffUser]

    def get_queryset(self):
        """ list to public-only."""
        queryset = Company.objects.filter(is_active= True)
        return queryset

    def perform_create(self,serializer):
        """Create company sector."""
        company=serializer.save()
