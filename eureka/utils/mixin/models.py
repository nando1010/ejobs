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




    # def validate_csv(value):
    #     # Probably worth doing this check first anyway
    #     if not value.name.endswith('.csv'):
    #         raise ValidationError('Invalid file type')
    #
    #     with open(value.file, 'r') as csvfile:
    #         try:
    #             csvreader = csv.reader(csvfile)
    #             # Do whatever checks you want here
    #             # Raise ValidationError if checks fail
    #                 if len(company_ruc)
    #             print("Hola")
    #         except csv.Error:
    #             raise ValidationError('Failed to parse the CSV file')
    #

    # company_ruc = forms.CharField(
    #     label='Company RUC',
    #     widget=forms.TextInput
    # )
    # company_name = forms.CharField(
    #     label='Company Name',
    #     widget=forms.TextInput
    # )
    # title = forms.CharField(
    #     label='Title',
    #     widget=forms.TextInput
    # )
    # description = forms.CharField(
    #     label='Description',
    #     widget=forms.Textarea
    # )
    # requeriments = forms.CharField(
    #     label='Requeriments',
    #     widget=forms.Textarea
    # )
    # contact_email = forms.EmailField(
    #     label='Contact email',
    #     widget=forms.EmailInput
    # )
    # location = forms.CharField(
    #     label='Location',
    #     widget=forms.TextInput
    # )
    # is_active = forms.BooleanField(
    #     label='Job is active',
    #     widget=forms.CheckboxInput
    # )
    # is_verified = forms.BooleanField(
    #     label='Job is verified',
    #     widget=forms.CheckboxInput
    # )
    # is_public = forms.BooleanField(
    #     label='Job is public',
    #     widget=forms.CheckboxInput
    # )
    # show_recruiter = forms.BooleanField(
    #     label='Recruiter is showed',
    #     widget=forms.CheckboxInput
    # )
    # website_url = forms.URLField(
    #     label='website_url',
    #     widget=forms.CheckboxInput
    # )
    # benefits = forms.CharField(
    #     label='Job is active',
    #     widget=forms.Textarea
    # )
    # urgency = forms.CharField(
    #     label='Urgency',
    #     widget=forms.Textarea
    # )
    # schedule = forms.CharField(
    #     label='Job is active',
    #     widget=forms.Textarea
    # )
    # comment = forms.CharField(
    #     label='Comments',
    #     widget=forms.Textarea
    # )
    # min_salary = forms.IntegerField(
    #     min_value=0,
    #     label='Min Salary',
    #     widget=forms.TextInput
    # )
    # max_salary = forms.IntegerField(
    #     min_value=0,
    #     label='Max Salary',
    #     widget=forms.TextInput
    # )
    #
    # """Variables estaticas"""
    # MONTHLY = "monthly"
    # ANNUAL = "annual"
    #
    # SALARY_RANGE_PERIOD =[
    #     ("monthly",'al mes'),
    #     ("annual",'al año'),
    # ]
    # pay_range_period = forms.ChoiceField(
    #     choices=SALARY_RANGE_PERIOD,
    #     label='Salary Range Period',
    #     widget=forms.Select
    # )
    #
    # class Meta:
    #     model = Job
    #     fields = (
    #
    #     )

    # class Method1(models.Model):
    #     inputfile = models.FileField(validators=[validate_csv])
    #
