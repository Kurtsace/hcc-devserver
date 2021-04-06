from django.forms import ModelForm, HiddenInput
from .models import SafewayLocation, RequestLogURL

# Create new safeway location form
class NewLocationForm(ModelForm):
    
    class Meta: 
        
        # Model 
        model = SafewayLocation
        
        # Fields 
        fields = ['location_name', 'fax_number', 'user']
        
        # Hidden fields 
        widgets = {
            'user' : HiddenInput(),
        }