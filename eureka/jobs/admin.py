"""Jobs admin."""

#Django
from django.contrib import admin

# Django import-export
from import_export.admin import ImportExportModelAdmin

# Model
from eureka.jobs.models import Job

# Resource
from eureka.jobs.resources import JobResource

# @admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    """Job admin."""

    resource_class = JobResource

    list_display = (
        'company_ruc',
        'company_name',
        'title',
        'description',
        'requeriments',
        'contact_email',
        'location',
        'is_active',
        'website_url',
        'benefits',
        'urgency',
        'schedule',
        'comment',
        'finished_at',
        'applications_made',
        'is_public',
        'show_recruiter'
    )

    search_fields = (
        'pk',
        'company_ruc',
        'company_name',
        'title',
        'location',
        'description',
        'requeriments',
        'finished_at',
        'min_salary',
        'max_salary'
    )

    list_filter = (
        'is_active',
        'is_public',
        'show_recruiter'
    )

    readonly_fields=[
        'applications_made',
    ]

admin.site.register(Job, JobAdmin)
