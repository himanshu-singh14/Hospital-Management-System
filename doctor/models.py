from django.db import models
from patient.models import Patient
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Prescription(models.Model):
    prescription = models.TextField(null=True, blank=True)
    symptoms = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symptoms


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gen = (('Male',"MALE"),('Female',"FEMALE"),('Others',"OTHERS"))
    gender = models.CharField("Gender ", max_length=10, blank=True, null=True, choices=gen,)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    st = (('Active',"ACTIVE"),('Inactive',"INACTIVE"))
    status = models.CharField("Status ", max_length=10, choices=st, blank=True, null=True)
    salary = models.IntegerField("Salary ", blank=True, null=True)
    dt = (('Neurology',"NEUROLOGY"),('Cardiology',"CARDIOLOGY"),('Emergency',"EMERGENCY"))
    department = models.CharField("Department ", max_length=20, choices=dt, blank=True, null=True)


    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def user_is_created(sender, instance, created, **kwargs):
#     if created:
#         Doctor.objects.create(user=instance)
#     else:
#         instance.doctor.save()