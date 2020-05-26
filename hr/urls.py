from django.urls import path
from .views import *

urlpatterns = [
    path('hr_dashboard/', hrDashboard, name='hr-dashboard'),
    path('create_payment/', createPayment, name='create-payment'),
    # path('create_patient/', createPatient, name='create-patient'),
    path('accounting/', accounting, name='accounting'),
    # path('hr_dashboard', hrDashboard, name='hr-dashboard'),

]