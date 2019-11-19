"""Jobs URLs."""

#Django
from django.urls import include,path

#Django REST framework
from rest_framework.routers import DefaultRouter

#Views
from .views import jobs as job_views
from .views import applications as application_views

router = DefaultRouter()
router.register(r'jobs',job_views.JobViewSet,basename='job')
router.register(r'jobs/(?P<pk>[^/.]+)/applications',application_views.ApplicationViewSet,basename='application')

urlpatterns=[
    path('',include(router.urls))
]
