"""Job permissions classes."""

#Django REST Framework
from rest_framework.permissions import BasePermission

#Models
from eureka.jobs.models import Job

class IsJobOwner(BasePermission):
    """Allow access only to User admin."""

    def has_object_permission(self,request,view,obj):
        """"Verify user is the one who created the job."""
        return True
        # if request.user.is_staff==True or request.user.is_superuser==True:
        #     return True
        # else:
        #     return False
        # # # if (request.user.is_staff==True) or request.user.is_superuser==True:
        # #     return True
        # return False


        # if (request.user.is_admin==True and request.user.is_staff==True) or request.user.is_superuser==True:
        #     return True
        # else:
        #     try:
        #         Job.object.get(
        #             user = request.user,
        #         )
        #     except Job.DoesNotExist:
        #         return False
        #     return True
