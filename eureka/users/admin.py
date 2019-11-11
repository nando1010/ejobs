"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models
from eureka.users.models import User,Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email','username','first_name','last_name','is_staff','is_client')
    list_filter =('is_client','is_staff','created','modified')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""
    list_display = ('user','jobs_applied','jobs_created','active_search')
    search_fields = ('user__email','user__first_name','user__last_name')
    list_filter = ('active_search',)


admin.site.register(User,CustomUserAdmin)