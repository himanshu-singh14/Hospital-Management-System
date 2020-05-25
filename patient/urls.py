from django.urls import path
from .views import *

urlpatterns = [
    path('patient_profile/<slug:username>/', patientProfile, name='patient-profile'),
    path('appointments/', appointments, name='appointments'),
    path('invoive_and_payments/', invoiveAndPayments, name='invoive-and-payments'),
    path('medical_history/', medicalHistory, name='medical-history'),
]