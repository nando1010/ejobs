"""Mixin utilities."""

#Django
from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError

#Models
from eureka.jobs.models import Job


#Utils
import csv

class ExportCsvMixin:
    """Allows export queryset to a CSV file."""
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class CsvImportForm(forms.Form):
    """Base form to import data from a CSV file."""
    csv_file = forms.FileField()
