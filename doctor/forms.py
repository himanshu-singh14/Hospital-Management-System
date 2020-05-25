from django import forms
from .models import Prescription
from django.contrib.auth.models import User
from .models import Doctor

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('symptoms', 'prescription', 'patient',)



class DoctorForm(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = ('name','phone','email','is_male','is_female','is_other','age',
                'address','blood_group','medical_report','case_paper')
