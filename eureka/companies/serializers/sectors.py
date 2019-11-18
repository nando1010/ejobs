"""Sector Serializers."""

#Django REST Framework
from rest_framework import serializers

#Models
from eureka.companies.models import Sector

class SectorModelSerializer(serializers.ModelSerializer):
    """Sector model serializer."""

    class Meta:
        """Meta.class."""

        model = Sector
        fields= ('id','name','description')
