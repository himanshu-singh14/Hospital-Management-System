from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .forms import PatientForm
from .models import Patient

# Create your views here.


def patientProfile(request, username=None):
    user1 = get_object_or_404(User, username=username)
    patient = get_object_or_404(Patient, user__username=user1)    # patient = Patient.objects.filter(user__username = user1)
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'patient/profile.html', {'patient_form': patient_form})
    else:
        if user1.username == patient.user.username:
            patient_form = PatientForm(instance=patient)
            return render(request, 'patient/profile.html', {'patient_form': patient_form})
        else:
            return HttpResponseRedirect(reverse('home'))


def appointments(request):
    context = {}
    context['apps'] = Appointment.objects.filter(patient=user.username)
    return render(request, 'patient/appointments.html', context)


def invoiveAndPayments(request):
    pass


def medicalHistory(request):
    pass

