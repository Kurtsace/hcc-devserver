from django.urls import path, include
from .views import UploadFile, UpdateFileDetails, UpdateFile, DeleteFile, FileList, FileDetail

app_name = 'file_upload'

urlpatterns = [
    
    #CRUD Views
    path('upload/', UploadFile.as_view(), name='upload_file'),
    path('update_file/<slug:slug>/', UpdateFile.as_view(), name='update_file'),
    path('update_file_details/<slug:slug>/', UpdateFileDetails.as_view(), name='update_file_details'),
    path('delete_file/<slug:slug>', DeleteFile.as_view(), name='delete_file'),
    
    #Views 
    path('file_list/', FileList.as_view(), name='file_list'),
    path('file/<slug:slug>/', FileDetail.as_view(), name='file_detail')
]
