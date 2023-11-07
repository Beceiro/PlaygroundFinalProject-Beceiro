from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images.png',upload_to='users/', null = True)
    link = models.URLField(null=True, blank=True)
    description = RichTextField()
    
    def __str__(self):
        return f'{self.user.username} Profile {self.user.first_name} {self.user.last_name} - {self.user.email}'