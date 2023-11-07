from django.contrib import admin
from app_coder.models import Record
from accounts.models import Profile

admin.site.register(Record)
admin.site.register(Profile)

