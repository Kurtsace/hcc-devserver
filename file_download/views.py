from django.shortcuts import render, get_object_or_404
from django.views import generic
from file_upload.models import File
from django.http import FileResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
import os 

# Create your views here.
class FileDownload(generic.View):

    #Get request
    def get(self, request, slug):
        
        #Get the file object if it exists
        file = get_object_or_404(File, slug=slug)
        
        #Get the file path
        file_path = file.uploaded_file.path
        
        #Get the file name
        file_name = os.path.basename(file.uploaded_file.path)
        
        #Make sure the ext is an allowed file extension
        #This is already checked beforehand in uploading the file but need to make sure 
        #This will prevent downloading anything in the file system other than whats specified
        ext = file_name.split('.')[-1]
        
        if ext in ['exe', 'rar', 'zip']:
            
            #Create a file response object and read in bytes 
            response = FileResponse( open(file_path, 'rb') )
            
            #Set content type to octet-stream
            response['content-type'] = 'application/octet-stream'
            
            #Set the content disposition to be handled by the browser 
            response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
            
            #Return the response 
            return response
        else:
            return Http404