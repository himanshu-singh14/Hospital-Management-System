from django.urls import path
from .views import *

urlpatterns = [
    path('doctor_profile/<slug:username>/', doctorProfile, name='doctor-profile'),
    path('appointments/', appointments, name='appointments'),
    path('prescriptions/', prescriptions, name='prescriptions'),
    path('create_prescriptions/', createPrescriptions, name='create-prescriptions'),
]