from django.shortcuts import render
from .forms import AppointmentForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Appointment
from patient.models import Patient
from patient.forms import PatientForm
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    context = {}
    context['apps'] = Appointment.objects.all()
    context['patients'] = Patient.objects.all()
    context['all'] = Appointment.objects.all().count()
    context['comp'] = Appointment.objects.filter(status="Completed").count()
    context['pen'] = Appointment.objects.filter(status="Pending").count()
    return render(request, 'receptionist/dashboard.html', context)


def createAppointment(request):
    if request.method == 'POST':
        app_form = AppointmentForm(request.POST)
        if app_form.is_valid():
            app_form.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'receptionist/create_appointment.html', {'app_form': app_form})
    else:
        app_form = AppointmentForm()
        return render(request, 'receptionist/create_appointment.html' , {'app_form': app_form})


def createPatient(request):
    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, 'receptionist/create_patient.html', {'patientform': patient_form})
    else:
        patient_form = PatientForm()
        return render(request, 'receptionist/create_patient.html' , {'patient_form': patient_form})


def deletePatient(request, username=None):
    user = get_object_or_404(User, username=username) 
    user.delete()
    return HttpResponseRedirect(reverse('dashboard'))


