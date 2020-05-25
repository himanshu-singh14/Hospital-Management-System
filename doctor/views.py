from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from patient.forms import PatientForm
from patient.models import Patient
from .models import Prescription
from .forms import PrescriptionForm

# Create your views here.

def appointments(request):
    pass


def prescriptions(request):
    context = {}
    context['prescriptions'] = Prescription.objects.all()
    return render(request, 'doctor/prescriptions.html', context)


def createPrescriptions(request):
    if request.method == 'POST':
        pres_form = PrescriptionForm(request.POST)
        if pres_form.is_valid():
            pres_form.save()
            return HttpResponseRedirect(reverse('prescriptions'))
        else:
            return render(request, 'doctor/create_prescriptions.html', {'pres_form': pres_form})
    else:
        pres_form = PrescriptionForm()
        return render(request, 'doctor/create_prescriptions.html' , {'pres_form': pres_form})





def doctorProfile(request, username=None):
    user1 = get_object_or_404(User, username=username)
    patient = get_object_or_404(Patient, user__username=user1)  
      # patient = Patient.objects.filter(user__username = user1)
    print(user1)
    print(patient)
    if request.method == 'POST':
        print("111111")
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            print("2222222")
            patient_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print("33333")
            return render(request, 'doctor/profile.html', {'doctor_form': patient_form})
    else:
        if user1.username == patient.user.username:
            print('99999999999999999999999')
            patient_form = PatientForm(instance=patient)
            return render(request, 'doctor/profile.html', {'doctor_form': patient_form})
        else:
            return HttpResponseRedirect(reverse('home'))
