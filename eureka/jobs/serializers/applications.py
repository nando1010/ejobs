"""Applications serializers."""

#Django
from datetime import datetime, timedelta

# Django Framework
from rest_framework import serializers

# Model
from eureka.jobs.models import Job
from eureka.jobs.models import Application
from eureka.users.models import User
from eureka.users.models import Profile


#Serialies
from eureka.users.serializers import UserModelSerializer,ProfileModelSerializer
from eureka.jobs.serializers import JobModelSerializer

#Utils
from django.utils import timezone


class CreateApplicationSerializer(serializers.ModelSerializer):
    """Create application serializer."""

    class Meta:
        """Meta class."""

        model = Application
        exclude= ('job','candidate_user','candidate_profile')

    def validate(self,data):
        """Verificar que el usuario no haya postulando antes a la convocatoria."""
        job = self.context['job']
        user = self.context['request'].user
        if user==None:
            return data
        else:
            q = Application.objects.filter(job = job, candidate_user=user)
            if q.exists():
                raise serializers.ValidationError('Usted ya ha postulado a esta vacante')
            return data

    def create(self,data):
        """Create application and update_stats."""

        job = self.context['job']
        user = self.context['request'].user
        profile = user.profile

        #Job
        job.applications_recived += 1
        data['application_order'] = job.applications_recived
        job.save()

        #User
        user.jobs_applied +=1
        user.save()

        #Application
        application = Application.objects.create(**data,job=job,candidate_user=user,candidate_profile=profile)

        return application

class ApplicationModelSerializer(serializers.ModelSerializer):
    """Create application serializer."""

    class Meta:
        """Meta class."""

        model = Application
        fields ='__all__'
