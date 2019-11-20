"""Job admin."""

# Django
from django.contrib import admin

# Model
from eureka.jobs.models import Job
from eureka.users.models import User
from eureka.users.models import Profile

# Utilities
import csv
from django.utils import timezone
from datetime import datetime, timedelta

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """Job admin."""

    list_display =(
        # 'created_by_user',
        # 'created_by_profile',
        # 'id',
        'company_ruc',
        'company_area',
        'company_sub_area',
        'company_role',
        'contract_type',
        'title',
        'description',
        'requeriments',
        'contact_email',
        'location',
        'is_active',
        # 'applications_recived',
        # 'is_public',
        # 'is_verified',
        # 'show_recruiter',
        # 'website_url',
        # 'benefits',
        # 'urgency',
        # 'work_schedule',
        # 'comment',
        # 'finished_at',
        # 'min_salary',
        # 'max_salary',
        # 'pay_range_period'
    )

    # search_fields = (
    #     'company_ruc',
    #     'company_area',
    #     'company_sub_area',
    #     'company_role',
    #     'contract_type',
    #     'title',
    # )
    #
    # list_filter = (
    #     'is_active',
    #     'applications_recived',
    #     'is_public',
    #     'is_verified',
    #     'show_recruiter'
    # )

    # actions = ['make_verified','make_unverified']
    #
    # def make_verified(self,request,queryset):
    #     """Make jobs verified."""
    #     queryset.update(is_verified=True)
    # make_verified.short_description = 'Make selected jobs verified'
    #
    # def make_unverified(self, request, queryset):
    #     """Make jobs unverified."""
    #     queryset.update(is_verified=False)
    # make_unverified.short_description = 'Make selected jobs unverified'
