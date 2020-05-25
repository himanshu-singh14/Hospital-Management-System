from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
from home.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'home/home.html')


# This API is showing the about page
def about(request):
	return render(request, 'home/about.html')


# This API is for take input from contact page
def contact(request):
	if request.method == 'POST':
		# Fetch all items which is taken from contact page
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		content = request.POST['content']

		# Check the corrctness of creditials
		if len(name)<2 or len(email)<3 or len(phone)<5 or len(content)<4:
			# Shows message if above condition is true
			messages.error(request, 'Please fill the form correctly')
		else:
			messages.success(request, 'Your issue has been Successfully sent.')
			# Assign all credentials or inputs to items of models
			contact = Contact(name=name, email=email, phone=phone, content=content)
			# Save in database of model contact
			contact.save()
		return render(request, 'home/contact.html')
	else:
		return render(request, 'home/contact.html')


# This API is for handle the signup page
def register(request):
    if request.method == 'POST': 
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('user-login'))
        else:
            return render(request, 'home/register.html', {'user_form': user_form})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'home/register.html', context)



# This API is for handle the login page
def userLogin(request):
    if request.method == 'POST':
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):          # It is important
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('home'))
        else:
            context['error'] = 'Please provide valid credentials !!'
            return render(request, 'home/login.html', context)
    else:
        return render(request, 'home/login.html')




def userLogout(request):
    if request.method == 'POST':
        print(request)
        logout(request)
        return HttpResponseRedirect(reverse('home'))
