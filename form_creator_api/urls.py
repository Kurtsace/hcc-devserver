from . import views 
from django.urls import path 
from django.contrib.admin.views.decorators import staff_member_required

# app name 
app_name = 'form_creator_api'

urlpatterns = [
    path('', staff_member_required( views.APIHomeView.as_view() ), name='api_home_view'),
    path('new_location/', staff_member_required( views.CreateSafewayLocation.as_view() ), name='create_safeway_location'),
    path('update_location/<int:pk>/', staff_member_required( views.UpdateSafewayLocation.as_view() ), name='update_safeway_location'),
    path('delete_location/<int:pk>/', staff_member_required( views.DeleteSafewayLocation.as_view() ), name='delete_safeway_location'),
    path('update_request_log_url/<int:pk>/', staff_member_required( views.UpdateRequestLogURL.as_view() ), name='update_request_log_url')
]