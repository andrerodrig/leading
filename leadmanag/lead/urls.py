from rest_framework import routers
from lead.resources import LeadViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
