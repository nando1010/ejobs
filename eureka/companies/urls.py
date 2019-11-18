"""Companies URL's."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

#Views
from .views import sectors as sector_views
from .views import companies as company_views

router = DefaultRouter()
router.register(r'sectors',sector_views.SectorViewSet,basename='sector')
router.register(r'companies',company_views.CompanyViewSet,basename='company')

urlpatterns=[
    path('',include(router.urls))
]
