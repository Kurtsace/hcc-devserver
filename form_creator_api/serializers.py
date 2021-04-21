from rest_framework import serializers 
from .models import SafewayLocation

# SafewayLocation serializer 
class SafewayLocationSerializer(serializers.ModelSerializer):
    
    # Meta 
    class Meta: 
        
        # Model 
        model = SafewayLocation
        
        # Fields 
        fields = ['location_name', 'fax_number']