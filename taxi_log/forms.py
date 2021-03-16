from django import forms

from .models import TaxiOrder

#Order form
class OrderForm(forms.ModelForm):
    
    #Init 
    def __init__(self, *args, **kwargs):
        
        #Call the super method to get the field set 
        super(OrderForm, self).__init__(*args, **kwargs)
        
        # Get the instance 
        instance = getattr(self, 'instance', None)
        
        # Set read only field 
        if instance and instance.pk:
            self.fields['order_number'].widget.attrs['readonly'] = True
            
        #Edit the required fields 
        self.fields['confirmation_number'].required = True
        self.fields['request_log_id'].required = True
    
    # Santiize read only input 
    def clean_order_number(self):
        
        # Get instance 
        instance = getattr(self, 'instance', None)
        
        if instance and instance.pk:
            return instance.order_number
        else:
            return self.cleaned_data['order_number']
    
    #Meta class 
    class Meta:
        
        #Model
        model = TaxiOrder 
        
        #Fields 
        fields = ['order_number', 'confirmation_number', 'request_log_id']