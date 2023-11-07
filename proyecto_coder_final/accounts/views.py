from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, EditUserForm
from .models import Profile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password = password)
			login(request, user)
			profile_user = Profile.objects.get_or_create(user = user)
			messages.success(request, "You have successfully registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'registration/register.html', {'form':form})

	return render(request, 'registration/register.html', {'form':form})

def login_user(request):
	if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, "You have been logged in!")
				return redirect('home')
			else:
				messages.success(request, "There was an error logging in, please try again...")
				return redirect('registration/login.hmtl')
	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out!")
	return redirect('home')

@login_required(login_url='/login')
def update_profile(request):
		current_user = Profile.objects.get(user_id = request.user.id)
		if request.method == 'POST':
			form = EditUserForm(request.POST or None, request.FILES or None, instance = current_user)
			if form.is_valid():
				form.save()
				if form.cleaned_data['first_name']:
					current_user.user.first_name = form.cleaned_data['first_name']
				if form.cleaned_data['last_name']:
					current_user.user.last_name = form.cleaned_data['last_name']
				if form.cleaned_data['email']:
					current_user.user.email = form.cleaned_data['email']
				current_user.link = form.cleaned_data['link']
				current_user.description = form.cleaned_data['description']
				if form.cleaned_data['image']:
					current_user.image = form.cleaned_data['image']
				current_user.save()
				current_user.user.save()
				login(request, current_user.user)
				messages.success(request, ("Your profile has been updated"))
				return redirect('home')
			return render(request, 'registration/update_profile.html', {'form': form, 'user_info': current_user.user, 'current_user': current_user})
		else:
			form = EditUserForm(request.POST or None, request.FILES or None, instance = current_user)
			return render(request, 'registration/update_profile.html', {'form': form, 'user_info': current_user.user, 'current_user': current_user})