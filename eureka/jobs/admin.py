"""Jobs admin."""
#Ptyhon
import string

#Django
from django import forms
from django.contrib import admin
from django.core import exceptions
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render,redirect

#Forms
#Models
from eureka.jobs.models import Job

#Utils
import csv,io

#Utilities
from eureka.utils.validators.models import validate_fields
from eureka.utils.mixin.models import ExportCsvMixin, CsvImportForm

@admin.register(Job)
class JobAdmin(admin.ModelAdmin, ExportCsvMixin):
    """Job admin."""

    fieldsets = (
        ('Codigo de Vacante', {'fields': ('id',)}),
        ('Datos empresa', {'fields': ('company_ruc','company_name',)}),
        ('Datos de la vacante', {'fields': ('title','location','description','requeriments','contact_email','urgency')}),
        ('Remuneracion y beneficios', {'fields': ('benefits','schedule','min_salary','max_salary','pay_range_period',)}),
        ('Informacion adicional', {'fields': ('website_url','comment')}),
        ('Estatus', {'fields': ('is_active','applications_made','is_verified','is_public','show_recruiter')}),
        ('Historial', {'fields': ('created','modified')}),
    )
    search_fields = ('id','company_ruc','company_name','title','location','description','requeriments','finished_at','min_salary','max_salary')
    ordering = ('company_name','title')
    list_display = ('id','company_ruc','company_name','title','description','requeriments','contact_email',
                    'location','is_active','website_url','benefits','urgency','schedule','comment','finished_at','applications_made','is_public','show_recruiter')
    list_filter = ('is_active','is_public','show_recruiter')
    readonly_fields=[
        'applications_made',
        'created',
        'modified',
        'is_active',
        'id'
    ]

    #Export CSV File adding in action dropdown
    actions = ["export_as_csv"]

    #Import CSV File
    change_list_template="admin/jobs/jobs_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            #...
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            # let's check if it is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')

            reader = csv_file.read().decode('UTF-8')

            # setup a stream which is when we loop through line
            # we are able to handle a data in a stream
            io_string = io.StringIO(reader)
            next(io_string)

            rows = csv.reader(io_string,delimiter=',',quotechar="'")

            # Pendiente de incluir funcion para contar el numero de filas
            # registros_totales =0
            fila = 0
            ok_error_status = False
            ok_errors={}

            for row in rows:
                """Variables iniciales."""
                new_values={}
                ok_errors={}

                """Convierte todos los vacios en Null."""
                n = 0
                while n < len(row):
                    if row[n] =='':
                        row[n]= None
                    n = n+1

                """
                Valida cada campo de cada fila segun lo declarado en el modelo.
                Devuelve:
                    - Un diccionario con los errores
                    - #Fila analizada
                    - Un diccionario key:value
                    - Status de Error: True or False
                """
                dict_results = validate_fields(row,fila,new_values)
                ok_errors = dict_results['errors']
                ok_fila = dict_results['fila']
                ok_values = dict_results['new_values']
                ok_error_status = dict_results['error_status']

                """Valida que el status error sea False"""
                if ok_error_status == False:
                    """Validamos si existe o no el registro en la BD."""
                    try:
                        """Si existe el registro, se actualiza."""
                        obj = Job.objects.get(id= ok_values['id'])
                        for key, value in ok_values.items():
                            setattr(obj,key,value)
                        obj.save()
                    except Job.DoesNotExist:
                        """Si no existe el registro, se crea."""
                        obj = Job(**ok_values)
                        obj.save()
                else:
                    """En caso el status de error sea True
                    salimos del bucle
                    """
                    break
                #Contador del numero de registro en evaluacion
                fila = fila +1

            if ok_error_status==False:
                registros_procesados=fila
                mensaje = 'Registros procesados {}'.format(registros_procesados)
            else:
                registros_procesados = ok_fila
                registro_errado = ok_fila + 1
                mensaje = 'Registro {} contiene errores, revisar: {}. Registros procesados {}'.format(registro_errado,ok_errors,registros_procesados)

            context={}

            self.message_user(request, mensaje)
            return redirect("..")

        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/jobs/csv_form.html", payload)
