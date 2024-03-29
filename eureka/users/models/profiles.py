"""Profile model."""

# Django
from django.db import models

#Utilities
from eureka.utils.models import EurekaModel

class Profile(EurekaModel):
    """Profile model.

    A profile holds a user's public data like biography, picture
    and statistics.
    """

    user = models.OneToOneField('users.User',on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile_picture',
        upload_to = 'users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank = True)

    # Stats
    jobs_applied = models.PositiveIntegerField(default = 0)
    jobs_created = models.PositiveIntegerField(default = 0)

    # Status
    active_search = models.BooleanField(default = True)

    def __str__(self):
            """Return user's str representation."""
            return str(self.user)
