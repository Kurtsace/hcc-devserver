from rest_framework import serializers 
from .models import SafewayLocation, RequestLogURL

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