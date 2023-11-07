from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from ckeditor.widgets import CKEditorWidget


# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* Email Address'}))
# 	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* First Name'}))
# 	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* Last Name'}))
# 	image = forms.ImageField(label="Picture", required=False)
# 	description = forms.CharField(required=False, widget=CKEditorWidget())

# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image', 'description')


# 	def __init__(self, *args, **kwargs):
# 		super(SignUpForm, self).__init__(*args, **kwargs)

# 		self.fields['username'].widget.attrs['class'] = 'form-control'
# 		self.fields['username'].widget.attrs['placeholder'] = '* Username'
# 		self.fields['username'].label = ''
# 		self.fields['username'].required = False
# 		self.fields['username'].help_text = '<small>You won\'t be able to change this in the future</small>'
  
# 		self.fields['password1'].widget.attrs['class'] = 'form-control'
# 		self.fields['password1'].widget.attrs['placeholder'] = '* Password'
# 		self.fields['password1'].label = ''

# 		self.fields['password2'].widget.attrs['class'] = 'form-control'
# 		self.fields['password2'].widget.attrs['placeholder'] = '* Confirm Password'
# 		self.fields['password2'].label = ''
  
# 		for field_name in ['username', 'password1', 'password2']: self.fields[field_name].help_text = None


class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")
	image = forms.ImageField(label="Picture", required=False)
	description = forms.CharField(required=False, widget=CKEditorWidget())

	class Meta:
		model = Record
		exclude = ('user',)
  
# class EditUserForm(UserChangeForm):
#     password = None
#     email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* Email Address'}))
#     first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* First Name'}))
#     last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'* Last Name'}))
#     image = forms.ImageField(required=False)
#     description = forms.CharField(required=False, widget=CKEditorWidget())
    
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'email', 'image', 'description')
#         help_texts = {campo: '' for campo in fields}
		# fields = ('user', 'image', 'description')

	# def __init__(self, *args, **kwargs):
    # 	super(EditUserForm, self).__init__(*args, **kwargs)