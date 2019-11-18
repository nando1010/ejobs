"""Sector models."""

#Django
from django.db import models

#Utilities
from eureka.utils.models import EurekaModel

class Sector(EurekaModel):
    """Company Sector model."""

    name = models.CharField(
        'Sector name',
        max_length = 100,
        unique = True,
        blank = False,
        help_text='Company Sector name'
    )

    description = models.TextField(
        'Sector description',
        blank = True,
        help_text='Description'
    )

    def __str__(self):
        """Return company sector detail."""
        return self.name

    class Meta(EurekaModel.Meta):
        """Meta class."""
