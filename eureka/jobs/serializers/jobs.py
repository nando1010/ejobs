"""Job serializers."""

# Django Framework
from rest_framework import serializers

# Model
from eureka.jobs.models import Job


class JobModelSerializer(serializers.ModelSerializer):
    """Job model serializer."""

    class Meta:
        """Meta class."""

        model = Job
        fields=(
            'company_ruc',
            'company_name',
            'title',
            'description',
            'requeriments',
            'contact_email',
            'location',
            'is_active',
            'applications_made',
            'is_public',
            'is_verified',
            'show_recruiter',
            'website_url',
            'benefits',
            'urgency'
            'schedule',
            'comment',
            'finished_at',
            'min_salary',
            'max_salary',
            'pay_range_period'
        )
