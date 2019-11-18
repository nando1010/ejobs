"""Sector models."""

#Django
from django.db import models

#Utilities
from eureka.utils.models import EurekaModel

class Company(EurekaModel):
    """Companies model."""

    """Foreign Keys"""
    sector = models.ForeignKey(
        'companies.Sector',
        on_delete = models.CASCADE,
    )

    """Informacion Obligatoria"""
    name = models.CharField(
        'razon social',
        max_length=200,
        blank=False
    )
    ruc = models.CharField(
        max_length=11,
        unique = True,
    )

    """Informacion Opcional"""
    trade_name = models.CharField(
        'nombre comercial',
        max_length=100,
        blank = True
    )

    description = models.TextField(blank = True, null = True)

    logo_url = models.URLField(blank = True, null = True)

    is_active = models.BooleanField(
        'company active',
        default = True
    )

    def __str__(self):
        """Return name."""
        return '@{} RUC: {}',format(
            self.name,
            self.ruc
        )

    class Meta(EurekaModel.Meta):
        """Meta class."""
