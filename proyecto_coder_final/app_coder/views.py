from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import AddRecordForm
from .models import Record
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
# def home(request):
# 	records = Record.objects.all()
# 	return render(request, 'app_coder/home.html', {'records':records})

class RecordView(TemplateView):
    template_name = 'app_coder/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = Record.objects.all()
        return context


class RecordDetail(DetailView):
    
    model = Record
    template_name = 'app_coder/record.html'
    context_object_name = 'customer_record'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Record.objects.get(id = self.kwargs.get('pk'))
        return context


# def customer_record(request, pk):
# 	if request.user.is_authenticated:
# 		customer_record = Record.objects.get(id=pk)
# 		return render(request, 'app_coder/record.html', {'customer_record':customer_record})
# 	else:
# 		messages.success(request, "You must be logged in to view that page...")
# 		return redirect('home')

@login_required(login_url='login')
def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record deleted successfully")
		return redirect('home')
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

@login_required(login_url='login')
def add_record(request):
	form = AddRecordForm(request.POST or None, request.FILES or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Record added correctly")
				return redirect('home')
		return render(request, 'app_coder/add_record.html', {'form':form})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

@login_required(login_url='login')
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, request.FILES or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record has been updated!")
			return redirect('home')
		return render(request, 'app_coder/update_record.html', {'form':form,})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')


def search_record(request):
	if request.user.is_authenticated:   
		if request.method == 'POST':
			searched = request.POST['searched']
			records = Record.objects.filter(first_name__contains=searched)
			return render(request, 'app_coder/search_record.html', {'searched':searched, 'records': records})
		else:
			return render(request, 'app_coder/search_record.html', {})
	else:
		messages.success(request, "You must be logged in")
		return redirect('home')

class AboutView(TemplateView):
    template_name = 'app_coder/aboutme.html'