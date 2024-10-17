from django.urls import path
from .api import TimeSlotViewSet, protected_view
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'timeslots', TimeSlotViewSet, basename='timeslot')

urlpatterns = [
    path('protected/',protected_view, name='protected_view'),

]
