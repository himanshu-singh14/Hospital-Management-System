from django.urls import path
from .views import *

urlpatterns = [
    path('hr_dashboard/', hrDashboard, name='hr-dashboard'),
    path('create_payment/', createPayment, name='create-payment'),
    path('accounting/', accounting, name='accounting'),
    path('delete_doctor/<slug:username>', deleteDoctor, name='delete-doctor'),

]