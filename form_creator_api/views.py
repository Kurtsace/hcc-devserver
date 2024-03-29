from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# DRF Imports 
from rest_framework.views import APIView 
from rest_framework.response import Response

# Serializers 
from .serializers import *

# Form
from .forms import NewLocationForm

#Import model
from .models import SafewayLocation, RequestLogURL
from file_upload.models import File

# Create your views here.

##########################################################
# API Response views 
##########################################################

# Api overview page 
class APIOverview(APIView):
    
    # Get request 
    def get(request, *args, **kwargs):
        
        # List of endpoints 
        api_endpoints = {
            'Safeway List' : '/safeway_list/',
            'Request Log URL' : '/request_log_url/',
            'Uploaded File Detail' : '/uploaded_files/<str:endpoint_name>'
        }
        
        # Return the response 
        return Response(api_endpoints)

# SafewayLocation List api view 
class SafewayLocationList(APIView):
    
    # Get request 
    def get(request, *args, **kwargs):
        
        # Query all objects 
        safeway_list = SafewayLocation.objects.all()
        
        # Serialize the model 
        serializer = SafewayLocationSerializer(safeway_list, many=True)
        
        # Return the serialized data 
        return Response(serializer.data)
    
# RequestLogURL api view 
class RequestLogDetail(APIView):
    
    # Get request 
    def get(self, *args, **kwargs):
        
        # Query the object 
        request_log_url = RequestLogURL.objects.first()
        
        # Serializer 
        serializer = RequestLogURLSerializer(request_log_url, many=False)
        
        # Return serialized data 
        return Response(serializer.data)
    
# Uploaded file api view
class UploadedFileDetail(APIView):
    
    # Get request 
    def get(self, *args, **kwargs):
        
        # Query provided object
        endpoint_name = self.kwargs['endpoint_name']
        uploaded_files = get_object_or_404(File, endpoint_name=endpoint_name)
        
        # Serialize the model 
        serializer = UploadedFileSerializer(uploaded_files, many=False)
        
        # Return serialized data 
        return Response(serializer.data)


##########################################################
# Model CRUD views
##########################################################

# API Home view 
class APIControlPanel(LoginRequiredMixin, generic.TemplateView):
    
    # Template
    template_name = 'form_creator_api/api_home_view.html'
    
    # Context dictionary 
    def get_context_data(self, *args, **kwargs):
        
         # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        # Pass in model objects into context 
        context['request_log_url'] = RequestLogURL.objects.first()
        context['safeway_location_list'] = SafewayLocation.objects.all()
        
        return context

# Create a new Safeway location
class CreateSafewayLocation(LoginRequiredMixin, generic.CreateView):
    
    # Template 
    template_name = 'form_creator_api/create_safeway_location.html'
    
    # Form 
    form_class = NewLocationForm
    
    # Model 
    model = SafewayLocation
    
    #Set field instances
    def get_initial(self):
        
        #Call super method 
        initial = super().get_initial()
        
        #Set user 
        initial['user'] = self.request.user
        
        return initial
    
# Update safeway location 
class UpdateSafewayLocation(LoginRequiredMixin, generic.UpdateView):
    
    # Template 
    template_name = 'form_creator_api/update_safeway_location.html'
    
    # Fields 
    fields = ['location_name', 'fax_number']
    
    # Model 
    model = SafewayLocation
    
# Delete safway location
class DeleteSafewayLocation(LoginRequiredMixin, generic.DeleteView):
    
    # Template 
    template_name = 'form_creator_api/confirm_delete.html'
    
    # Model 
    model = SafewayLocation
    
    # Redirect 
    def get_success_url(self):
        return reverse('form_creator_api:api_control_panel')
    
# Update Request Log URL
class UpdateRequestLogURL(LoginRequiredMixin, generic.UpdateView):
    
    # Template 
    template_name = 'form_creator_api/update_request_log_url.html'
    
    # Model 
    model = RequestLogURL
    
    # Fields 
    fields = ['url']
