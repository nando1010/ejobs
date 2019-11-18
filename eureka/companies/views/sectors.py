"""Sector views."""

#Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

#Permissions
from rest_framework.permissions import IsAuthenticated
from eureka.utils.permissions.maintenance import IsStaffUser

#Serializers
from eureka.companies.serializers import SectorModelSerializer

#Models
from eureka.companies.models import Sector, Company


class SectorViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Company Sector ViewSet."""

    serializer_class = SectorModelSerializer

    permission_classes = [IsAuthenticated,IsStaffUser]

    queryset = Sector.objects.all()

    def perform_create(self,serializer):
        """Create company sector."""
        sector=serializer.save()
