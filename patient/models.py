from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Profile

# Create your models here.


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gen = (('Male',"MALE"),('Female',"FEMALE"),('Others',"OTHERS"))
    gender = models.CharField("Gender ", max_length=10, blank=True, null=True, choices=gen, default='male')
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100,  blank=True, null=True)
    bg = (('O+',"O+ TYPE"),('O-',"O- TYPE"),('A+',"A+ TYPE"),('A-',"A- TYPE"),('B+',"B+ TYPE"))
    blood_group = models.CharField("Blood Group ", max_length=10, choices=bg, default='o+')
    medical_report = models.ImageField(upload_to='patient/images', blank=True, null=True)
    case_paper = models.IntegerField("Case Paper", blank=True, null=True)


    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
# def user_is_created(sender, instance, created, **kwargs):
#     if created:
#         Patient.objects.create(user=instance)
#     else:
#         instance.patient.save()
