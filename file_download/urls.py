from django.urls import path
from . import views

app_name = 'file_download'

urlpatterns = [
    path('download/<slug:slug>/', views.FileDownload.as_view(), name='download_file')
]
