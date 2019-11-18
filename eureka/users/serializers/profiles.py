"""Profile Serializer."""

#Django REST Framework
from rest_framework import serializers

#Models
from eureka.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile Model Serializer."""

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture',
            'biography',
            'active_search',
            'jobs_applied',
            'jobs_created'
        )
        read_only_fields = (
            'jobs_applied',
            'jobs_created'
        )
