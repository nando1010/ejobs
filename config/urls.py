"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('',include(('eureka.jobs.urls','jobs'),namespace = 'job')),
    path('',include(('eureka.users.urls','users'),namespace = 'users')),
    path('',include(('eureka.companies.urls','companies'),namespace = 'companies'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
