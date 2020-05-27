from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from patient.forms import PatientForm
from patient.models import Patient
from .models import Prescription
from .forms import PrescriptionForm
from .models import Doctor
from  .forms import DoctorForm
from receptionist.models import Appointment


def doctorAppointments(request):
    context = {}
    context['apps'] = Appointment.objects.filter(doctor__user__username = request.user)
    return render(request, 'doctor/doctor_appointments.html', context)


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
    doctor = get_object_or_404(Doctor, user__username=user1)   # patient = Patient.objects.filter(user__username = user1)
    print(user1)
    print(doctor)
    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'doctor/profile.html', {'doctor_form': doctor_form})
    else:
        if user1.username == doctor.user.username:
            doctor_form = DoctorForm(instance=doctor)
            return render(request, 'doctor/profile.html', {'doctor_form': doctor_form})
        else:
            return HttpResponseRedirect(reverse('home'))
