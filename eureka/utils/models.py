"""Django models utilities."""

# Django
from django.db import models

class EurekaModel(models.Model):
    """Eureka Jobs base model.

    EurekaModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following atributes:
        + created(Datetime): Stores the datetime on which object was created.
        + modified(Datetime): Stores the datetime on which object was modified.
    """

    created = models.DateTimeField(
        'create at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering =['-created','-modified']


class GenericModel(models.Model):
    """Generic base model.

    GenericModel acts as an abstract base class from which (Company
    and Jobs) Attributes related models in the project will inherit. This class provides
    every table with the following atributes:
        + name(CharField): Stores the object's name.
        + description(CharField): Stores the object's description.
    """
    name = models.CharField(
        'object name',
        max_length = 100,
        blank = False,
        help_text='Object name'
    )

    modified = models.TextField(
        'object description',
        blank = True,
        help_text='Object description'
    )

    class Meta:
        """Meta option."""

        abstract = True

        ordering =['name','description']
