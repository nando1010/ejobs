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

    users = models.OneToOneField('users.User',on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile_picture',
        upload_to = 'users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank = True)

    # Stats
    jobs_applied = models.PositiveIntegerField()
    jobs_created = models.PositiveIntegerField()

    def __str__(self):
            """Return user's str representation."""
            return str(self.user)
