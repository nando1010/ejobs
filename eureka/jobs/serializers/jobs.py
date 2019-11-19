"""Job serializers."""

#Django
from datetime import datetime, timedelta

# Django Framework
from rest_framework import serializers

# Model
from eureka.jobs.models import Job
from eureka.users.models import User
from eureka.users.models import Profile

#Serialies
from eureka.users.serializers import UserModelSerializer,ProfileModelSerializer

#Utils
from django.utils import timezone

class JobModelSerializer(serializers.ModelSerializer):
    """Job model serializer."""

    class Meta:

        model = Job
        fields=(
            'user',
            'profile',
            'id',
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
            'urgency',
            'schedule',
            'comment',
            'finished_at',
            'min_salary',
            'max_salary',
            'pay_range_period'
        )
        read_only_fields =(
            'is_active',
            'applications_made',
            'is_verified',
            'is_public',
        )

    def update(self, instance, data):
        """
        Verifica que la vacante no haya caducado
        En ningun caso, permite modificar la fecha de fin
        """
        now = timezone.now()
        data.pop('finished_at')
        if instance.finished_at <= now:
            raise serializers.ValidationError('La vacante ya caducó.')
        return super(JobModelSerializer, self).update(instance, data)


class CreateJobSerializer(serializers.ModelSerializer):
    """Create job serializer."""

    # user = UserModelSerializer(Read_only = True)

    def validate(self, data):
        """
        Verify finished date is not in the past
        En caso no ingrese ningun valor como fecha de fin,
        La duracion por default será 10 dias
        """
        min_date = timezone.now() + timedelta(days=1)
        standard_duration = timezone.now() + timedelta(days=10)

        if data.get('finished_at',None) == None:
            data['finished_at'] = standard_duration
        elif data['finished_at'] == "":
            data['finished_at'] = standard_duration
        elif data['finished_at'] < min_date:
            raise serializers.ValidationError(
                'La fecha de fin debe tener como minimo una ventana de 1 dia'
            )
        return data

    def create(self,data):
        """Create job and update_stats."""
        job = Job.objects.create(**data)
        return job

    class Meta:
        """Meta class."""

        model = Job
        fields=(
            'user',
            'profile',
            'id',
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
            'urgency',
            'schedule',
            'comment',
            'finished_at',
            'min_salary',
            'max_salary',
            'pay_range_period'
        )
        read_only_fields =(
            'is_active',
            'applications_made',
            'is_verified',
        )
