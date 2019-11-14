"""Jobs URLs."""

#Django
from django.urls import include,path

#Django REST framework
from rest_framework.routers import DefaultRouter

#Views
from .views import jobs as job_views

router = DefaultRouter()
router.register(r'jobs',job_views.JobViewSet,basename='job')

urlpatterns=[
    path('',include(router.urls))
]
