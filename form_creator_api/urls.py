from . import views 
from django.urls import path 
from django.contrib.admin.views.decorators import staff_member_required

# app name 
app_name = 'form_creator_api'

urlpatterns = [
    
    # Endpoints
    path('', views.APIOverview.as_view(), name='api_overview'),
    path('safeway_list/', views.SafewayLocationList.as_view(), name='safeway_list_api'),
    path('request_log_url/', views.RequestLogDetail.as_view(), name='request_log_api'),
    path('uploaded_files/<str:endpoint_name>/', views.UploadedFileDetail.as_view(), name='uploaded_files_api'),
    
    # Form views and template views
    path('control_panel/', staff_member_required( views.APIControlPanel.as_view() ), name='api_control_panel'),
    path('new_location/', staff_member_required( views.CreateSafewayLocation.as_view() ), name='create_safeway_location'),
    path('update_location/<int:pk>/', staff_member_required( views.UpdateSafewayLocation.as_view() ), name='update_safeway_location'),
    path('delete_location/<int:pk>/', staff_member_required( views.DeleteSafewayLocation.as_view() ), name='delete_safeway_location'),
    path('update_request_log_url/<int:pk>/', staff_member_required( views.UpdateRequestLogURL.as_view() ), name='update_request_log_url')
]