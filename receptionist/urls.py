from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    path('create_appointment/', createAppointment, name='create-appointment'),
    path('create_patient/', createPatient, name='create-patient'),
    path('delete_patient/<slug:username>', deletePatient, name='delete-patient'),
    path('hr_dashboard', hrDashboard, name='hr-dashboard'),

]

