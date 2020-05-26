from django.db import models
from patient.models import Patient

class Payment(models.Model):
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    fee = models.IntegerField(default=500)
    paid = models.IntegerField(default=300)
    outstanding = models.IntegerField(default=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.user.username
    

