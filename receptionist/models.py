from django.db import models
from patient.models import Patient
from doctor.models import Doctor

# Create your models here.

class Appointment(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    patient = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    st = (('pending',"PENDING"),('completed',"COMPLETED"))
    status = models.CharField("Status :", max_length=10, choices=st, default='pending')

    # def __str__(self):
    #     return self.patient
    
