"""Job Applications models."""

#DjangoTemplates
from django.db import models

#Utilities
from eureka.utils.models import EurekaModel

#Models
from eureka.users.models import User,Profile


class Application(EurekaModel):
    """Job Applications model."""
    """Datos Obligatorios"""
    candidate_first_name = models.CharField(max_length=50,blank=False)
    candidate_last_name = models.CharField(max_length=50,blank=False)
    candidate_email = models.EmailField(blank=False)
    cv_url = models.URLField(blank=True,null=True)

    """Variables estaticas"""
    MONTHLY = "monthly"
    ANNUAL = "annual"

    SALARY_RANGE_PERIOD =[
        (MONTHLY,'al mes'),
        (ANNUAL,'al año'),
    ]

    """Informacion Opcional"""
    candidate_cellphone = models.CharField(max_length=20,blank=True)
    min_salary = models.PositiveIntegerField(default=0,blank=True,null=True)
    max_salary = models.PositiveIntegerField(default=0,blank=True,null=True)
    pay_range_period = models.CharField(max_length=10,choices=SALARY_RANGE_PERIOD,blank=True,null=True)
    first_attachment = models.URLField(blank = True,null=True)

    """Estadisticas."""
    application_order = models.PositiveIntegerField(default=0)


    """Foreign Keys"""
    job = models.ForeignKey(
        'jobs.Job',
        on_delete = models.CASCADE,
    )

    candidate_user = models.ForeignKey(
        'users.User',
        null=True,
        on_delete = models.SET_NULL,
    )

    candidate_profile = models.ForeignKey(
        'users.Profile',
        null=True,
        on_delete = models.SET_NULL,
    )


    def __str__(self):
        """Return name."""
        return '{} by @{} on {}'.format(self.job, self.candidate_user,self.created)
