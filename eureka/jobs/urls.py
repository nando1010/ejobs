"""Jobs URLs."""

#Django
from django.urls import path

#Views
from eureka.jobs.views import list_jobs, create_job

urlpatterns = [
    path('jobs/', list_jobs),
    path('jobs/create/', create_job)
]
