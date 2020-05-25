from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This model is for our contact page in which we take input from users and store in database
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True , auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = (('doctor',"DOCTOR"),('patient',"PATIENT"))
    roles = models.CharField("Register as", max_length=10, choices=role, default='doctor')

    def __str__(self):
        return self.user.username