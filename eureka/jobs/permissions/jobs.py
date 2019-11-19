"""Job permissions classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Models
from eureka.jobs.models import Job

# Utilities
from datetime import timedelta
from django.utils import timezone


class IsJobOwner(BasePermission):
    """Allow access only to User admin."""

    def has_permission(self,request,view):
        return True
        """Let object permission grant access."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self,request,view,obj):
        """"Verify user is the one who created the job."""
        try:
            return request.user == obj.created_by_user
        except:
            return False


class IsJobActive(BasePermission):
    """Allow access only to Job Active admin."""

    def has_permission(self,request,view):
        return True
        """Let object permission grant access."""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self,request,view,obj):
        now = timezone.now()
        """"Verify user is the one who created the job."""
        try:
            return obj.job.finished_at>=now
        except:
            return False
