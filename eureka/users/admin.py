"""User models admin."""

# Django
from django.contrib import admin

#Models
from eureka.users.models import User,Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User model admin."""

    list_display = ('email','first_name','last_name','is_staff','is_client')
    list_filter =('is_client','is_staff','created','modified')
    readonly_fields=[
        'created',
        'last_login',
        'modified'
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""
    list_display = ('user','jobs_applied','jobs_created','active_search')
    search_fields = ('user__email','user__first_name','user__last_name')
    list_filter = ('active_search',)
