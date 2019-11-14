"""Job Serializers."""

#Django REST Framework
from rest_framework import serializers

#Models
from eureka.jobs.models import Job

class JobSerializer(serializers.Serializer):
    """Job serializer."""

    company_ruc = serializers.CharField()
    company_name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    requeriments = serializers.CharField()
    contact_email = serializers.EmailField()
    location = serializers.CharField()
    is_active = serializers.BooleanField()
    applications_made = serializers.IntegerField()
    website_url = serializers.URLField()
    benefits = serializers.CharField()
    urgency = serializers.CharField()
    schedule = serializers.CharField()
    comment = serializers.CharField()
    finished_at = serializers.DateTimeField()
    min_salary = serializers.IntegerField()
    max_salary = serializers.IntegerField()
    pay_range_period=serializers.CharField()
    created = serializers.DateTimeField()
    modified =serializers.DateTimeField()


class CreateJobSerializer(serializers.Serializer):
    """Create job serializer."""
    company_ruc = serializers.CharField(max_length=50)
    company_name = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    requeriments = serializers.CharField()
    contact_email = serializers.CharField()
    location = serializers.CharField(max_length=50)
    website_url = serializers.URLField(required = False, allow_blank=True)
    benefits = serializers.CharField(required = False, allow_blank=True)
    urgency = serializers.CharField(required = False, allow_blank=True)
    schedule = serializers.CharField(required = False, allow_blank=True)
    comment = serializers.CharField(required = False, allow_blank=True)
    min_salary = serializers.IntegerField(required = False)
    max_salary = serializers.IntegerField(required = False)
    is_public = serializers.BooleanField()

    """Variables estaticas"""
    MONTHLY = "monthly"
    ANNUAL = "annual"

    SALARY_RANGE_PERIOD =[
        (MONTHLY,'al mes'),
        (ANNUAL,'al año'),
    ]
    pay_range_period=serializers.ChoiceField(choices=SALARY_RANGE_PERIOD,required = False,allow_blank=True)

    def create(self,data):
        """Create job."""
        return Job.objects.create(**data)
