from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, AddRecordForm, EditUserForm
from .models import Record, Profile
from django.views.generic import TemplateView

def home(request):
	records = Record.objects.all()
	return render(request, 'home.html', {'records':records})

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
				return redirect('login')
	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out!")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have successfully registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to view that page...")
		return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record deleted successfully")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record added correctly")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, request.FILES or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form,})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')


def search_record(request):
	if request.user.is_authenticated:   
		if request.method == 'POST':
			searched = request.POST['searched']
			records = Record.objects.filter(first_name__contains=searched)
			return render(request, 'search_record.html', {'searched':searched, 'records': records})
		else:
			return render(request, 'search_record.html', {})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

def update_profile(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = EditUserForm(request.POST or None, request.FILES or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Your profile has been updated"))
            return redirect('home')
        return render(request, 'update_profile.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

class AboutView(TemplateView):
    template_name = "aboutme.html"