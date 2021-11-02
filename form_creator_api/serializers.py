from rest_framework import serializers 
from .models import SafewayLocation, RequestLogURL
from file_upload.models import File

# SafewayLocation serializer 
class SafewayLocationSerializer(serializers.ModelSerializer):
    
    # Meta 
    class Meta: 
        
        # Model 
        model = SafewayLocation
        
        # Fields 
        fields = ['location_name', 'fax_number']
        
# Request Log Url Serializer 
class RequestLogURLSerializer(serializers.ModelSerializer):
    
    # Meta 
    class Meta:
        
        model = RequestLogURL
        
        # Fields 
        fields = ['url']
        
# Uploaded File serializer 
class UploadedFileSerializer(serializers.ModelSerializer):
    
    # Meta 
    class Meta: 
        
        model = File 
        
        fields = ['file_name', 'version']
        
        lookup_field = 'file_name'
        
        lookup_url_kwarg = 'file_name'