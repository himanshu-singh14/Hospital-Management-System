from django.urls import path
from .views import *

urlpatterns = [
    path('patient_profile/<slug:username>/', patientProfile, name='patient-profile'),
    path('patient_appointments/', patientAppointments, name='patient-appointments'),
    path('invoice_and_payments/', invoiceAndPayments, name='invoice-and-payments'),
    path('medical_history/', medicalHistory, name='medical-history'),
]