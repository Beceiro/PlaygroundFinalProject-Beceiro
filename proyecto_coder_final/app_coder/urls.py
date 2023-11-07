from django.urls import path
from app_coder import views
from app_coder.views import AboutView, RecordView, RecordDetail

urlpatterns = [
    path('', RecordView.as_view(), name='home'),
    path('record/<int:pk>', RecordDetail.as_view(), name='record'),
    # path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('search_record/', views.search_record, name='search_record'),
    path('about/', AboutView.as_view(), name='aboutme'),
    # path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('update_profile/', views.update_profile, name='update_profile')
]
