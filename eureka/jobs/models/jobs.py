"""Job model."""

# Django
from django.db import models
from datetime import datetime, timedelta

#Utilities
from eureka.utils.models import EurekaModel
from eureka.users.models import User,Profile


class Job(EurekaModel):
    """Job model.

    A job is a job offer created by a recruiter-users
    where users can apply. Everyone can apply and share job.
    Only recruiters can create jobs.
    """

    """Foreign Keys """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE
    )


    """Datos Obligatorios"""
    company_ruc = models.CharField(max_length=11,blank=False)
    company_name = models.CharField(max_length=100,blank=False)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    requeriments = models.TextField(blank=False)
    contact_email = models.EmailField(blank=False)
    location = models.CharField(max_length=50,blank=False)

    """Estadisticas"""
    is_active = models.BooleanField(
        'Application is active',
        default = True,
        help_text='Acepta Postulaciones'
    )

    applications_made = models.PositiveIntegerField(
        'Aplications made',
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
    schedule = models.TextField(blank = True, null = True)
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
