from django.db import models
from patient.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Prescription(models.Model):
    prescription = models.TextField(null=True, blank=True)
    symptoms = models.CharField(max_length=100)
    patient = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symptoms


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_male = models.BooleanField("Male", default=False)
    is_female = models.BooleanField("Female", default=False)
    is_other = models.BooleanField("Other", default=False)
    age = models.IntegerField(default=20)
    address = models.CharField(max_length=100)
    bg = (('o+',"O+ TYPE"),('o-',"O- TYPE"),('a+',"A+ TYPE"),('a-',"A- TYPE"),('b+',"B+ TYPE"))
    blood_group = models.CharField("Blood Group", max_length=10, choices=bg, default='o+')
    medical_report = models.ImageField(upload_to='patient/images')
    case_paper = models.IntegerField("Case Paper", default=1)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)
    else:
        instance.doctor.save()