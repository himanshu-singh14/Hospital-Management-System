from django import forms
from django.contrib.auth.models import User
from .models import Patient


class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields = ('name','phone','email','gender','age',
                'address','blood_group','medical_report','case_paper')

    # label = {
        #     'password': "Password"
        # }

