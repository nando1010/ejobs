"""Job model."""

# Django
from django.db import models
from datetime import datetime, timedelta

#Utilities
from eureka.utils.models import EurekaModel

#Models
from eureka.users.models import User,Profile
from eureka.companies.models import Company


class Job(EurekaModel):
    """Job model.

    A job is a job offer created by a recruiter-users
    where users can apply. Everyone can apply and share job.
    Only recruiters can create jobs.
    """

    """Foreign Keys """
    created_by_user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE
    )

    created_by_profile = models.ForeignKey(
        'users.Profile', on_delete=models.CASCADE
    )

    company_ruc = models.ForeignKey(
        'companies.Company',
        null= True,
        to_field='ruc',
        on_delete=models.SET_NULL
    )


    """Datos Obligatorios"""
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    requeriments = models.TextField(blank=False)
    contact_email = models.EmailField(blank=False)
    location = models.CharField(max_length=50,blank=False)

    """Categorias de Busqueda"""
    #Posteriormente seran susbstituidos por ForeignKey
    company_area = models.CharField(max_length=100)
    company_sub_area = models.CharField(max_length=100)
    company_role = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100)

    """Estadisticas"""
    is_active = models.BooleanField(
        'Application is active',
        default = True,
        help_text='Acepta Postulaciones'
    )

    applications_recived = models.PositiveIntegerField(
        'Aplications recived',
        default = 0,
        help_text = 'Postulaciones realizadas'
    )

    """Estatus"""
    is_verified=models.BooleanField(
        'Convocatoria verificada',
        default = True,
        help_text = 'Determina si la oferta laboral ha sido verificada y corresponde a la empresa en mencion'
    )
    is_public=models.BooleanField(
        'Convocatoria publica',
        default = True,
        help_text = 'Determina si la oferta laboral es publica'
    )
    show_recruiter = models.BooleanField(
        'Mostrar Reclutador',
        default = True,
        help_text = 'Mostrar al reclutador que crea la oferta laboral'
    )

    """Informacion Opcional"""
    website_url = models.URLField(blank=True,null = True)
    benefits = models.TextField(blank = True, null = True)
    urgency = models.TextField(blank = True, null = True)
    work_schedule = models.TextField(blank = True, null = True)
    comment = models.TextField(blank = True, null = True)
    finished_at = models.DateTimeField(blank=True, null = True)

    """Variables estaticas"""
    MONTHLY = "monthly"
    ANNUAL = "annual"

    SALARY_RANGE_PERIOD =[
        (MONTHLY,'al mes'),
        (ANNUAL,'al año'),
    ]

    """Informacion Opcional Salario"""
    min_salary = models.PositiveIntegerField(blank=True,null=True)
    max_salary = models.PositiveIntegerField(blank=True,null=True)
    pay_range_period = models.CharField(max_length=10,choices=SALARY_RANGE_PERIOD,blank=True,null = True)


    def __str__(self):
        """Return name."""
        return '{} by @{}'.format(self.title, self.company_name)

    class Meta(EurekaModel.Meta):
        """Meta class."""
