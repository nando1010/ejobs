"""Job permissions classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Models
from eureka.jobs.models import Job

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
            return request.user == obj.user
        except:
            return False
