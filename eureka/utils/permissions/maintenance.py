"""Maintenance permission classes."""
#Django REST Framework
from rest_framework.permissions import BasePermission

#Models
from eureka.users.models import User

class IsStaffUser(BasePermission):
    """Allow access to Staff Users.

    Expect that the views implementing this permission
    are requested by a Staff User, having attribute is_staff ==True
    """

    def has_permission(self,request,view):
        """Verify user is an Staff User."""
        try:
            if request.user.is_staff:
                return True
        except request.user.DoesNotExist:
            return False
