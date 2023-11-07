from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/login/', views.login_user, name='login'),
    path('accounts/logout/', views.logout_user, name='logout'),
    path('accounts/register/', views.register_user, name='register'),
    path('accounts/profile/', views.update_profile, name='update_profile')
    ]