"""Company Serializers."""

#Django REST Framework
from rest_framework import serializers

#Models
from eureka.companies.models import Company
from eureka.companies.models import Sector

class CompanyModelSerializer(serializers.ModelSerializer):
    """Company model serializer."""

    class Meta:
        """Meta class."""

        model = Company
        fields= ('id','sector','ruc','name','trade_name','description')

    # def create(self,data):
    #     """Create a new Company."""
    #     company = Company.objects.create(**data)
    #     return company
