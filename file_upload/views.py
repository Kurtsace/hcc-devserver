from django.shortcuts import render
from django.urls import reverse
from .forms import UpdateFileForm, UploadFileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import File

# Create your views here.

#############################
# Generic Views
#############################

#File list view 
class FileList(generic.ListView):
    
    #Model 
    model = File 
    
    #Template 
    template_name = 'file_upload/file_list_view.html'
    
#File detail view 
class FileDetail(LoginRequiredMixin, generic.DetailView):
    
    #Model
    model = File 
    
    #Template 
    template_name = 'file_upload/file_detail_view.html'

#############################
# CRUD Views
#############################

#Upload file view
class UploadFile(generic.CreateView):
    
    #Form
    form_class = UploadFileForm
    
    #Model 
    model = File 
    
    #Template
    template_name = 'file_upload/file_upload_view.html'
    
    #Set field instances
    def get_initial(self):
        
        #Call super method 
        initial = super().get_initial()
        
        #Set user 
        initial['user'] = self.request.user
        
        return initial
    
#Update file view 
class UpdateFile(generic.UpdateView):
    
    #Form
    form_class = UpdateFileForm
    
    #Model 
    model = File 
    
    #Template 
    template_name = 'file_upload/update_file_view.html'

#Update file details view 
class UpdateFileDetails(generic.UpdateView):
    
    #Model 
    model = File 
    
    #Fields 
    fields = ['file_name', 'description', 'version']
    
    #Template
    template_name = 'file_upload/update_file_details_view.html'
    
#Delete file view 
class DeleteFile(generic.DeleteView):
    
    #Model 
    model = File 
    
    #Template
    template_name = 'file_upload/delete_file_view.html'
    
    #Redirect to home page 
    def get_success_url(self):
        return reverse('home')
    
