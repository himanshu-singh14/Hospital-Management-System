from django.urls import path
from .views import *

urlpatterns = [
    path('doctor_profile/<slug:username>/', doctorProfile, name='doctor-profile'),
    path('doctor_appointments/', doctorAppointments, name='doctor-appointments'),
    path('prescriptions/', prescriptions, name='prescriptions'),
    path('create_prescriptions/', createPrescriptions, name='create-prescriptions'),
]