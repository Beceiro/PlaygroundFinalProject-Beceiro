from django.db import models
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='images.png',upload_to='avatar/uploads/', null = True)
#     description = RichTextField(null=True, blank=True)
    
#     def __str__(self):
#         return f'{self.user.username} Profile'


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)
	image = models.ImageField(null=True, blank=True, upload_to='images/')
	description = RichTextField()

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")