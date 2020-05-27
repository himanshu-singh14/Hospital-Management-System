from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .forms import PatientForm
from .models import Patient
from receptionist.models import Appointment
from hr.models import Payment
from doctor.models import Prescription


def patientProfile(request, username=None):
    user1 = get_object_or_404(User, username=username)
    patient = get_object_or_404(Patient, user__username=user1)    # patient = Patient.objects.filter(user__username = user1)
    if request.method == 'POST':
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'patient/profile.html', {'patient_form': patient_form, 'username': username})
    else:
        if user1.username == patient.user.username:
            patient_form = PatientForm(instance=patient)
            return render(request, 'patient/profile.html', {'patient_form': patient_form, 'username': username})
        else:
            return HttpResponseRedirect(reverse('home'))


def patientAppointments(request):
    context = {}
    context['apps'] = Appointment.objects.filter(patient__user__username=request.user).all()
    return render(request, 'patient/patient_appointments.html', context)


def invoiceAndPayments(request):
    context = {}
    context['payments'] = Payment.objects.filter(patient__user__username=request.user).all()
    return render(request, 'patient/invoice_payments.html', context)


def medicalHistory(request):
    context = {}
    context['medi_all'] = Prescription.objects.filter(patient__user__username=request.user).all()
    return render(request, 'patient/medical_history.html', context)

