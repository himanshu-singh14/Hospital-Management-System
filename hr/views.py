from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from patient.models import Patient
from doctor.models import Doctor
from .models import Payment
from .forms import PaymentForm


def hrDashboard(request):
    context = {}
    context['docs'] = Doctor.objects.all()
    context['all_docs'] = Doctor.objects.all().count()
    context['all_pet'] = Patient.objects.all().count()
    context['active_doctor'] = Doctor.objects.filter(status="Active").count()
    return render(request, 'hr/hr_dashboard.html', context)


def accounting(request):
    context = {}
    context['payments'] = Payment.objects.all()
    return render(request, 'hr/accounting.html', context)


def createPayment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_form.save()
            return HttpResponseRedirect(reverse('accounting'))
        else:
            return render(request, 'hr/create_payment.html', {'payment_form': payment_form})
    else:
        payment_form = PaymentForm()
        return render(request, 'hr/create_payment.html' , {'payment_form': payment_form})

