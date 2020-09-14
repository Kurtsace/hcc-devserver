from django import forms

from .models import TaxiOrder

#Order form
class OrderForm(forms.ModelForm):
    
    #Set read only fields
    order_number = forms.IntegerField(disabled=True, min_value=0)
    
    #Init 
    def __init__(self, *args, **kwargs):
        
        #Call the super method to get the field set 
        super(OrderForm, self).__init__(*args, **kwargs)
        
        #Edit the required fields 
        self.fields['confirmation_number'].required = True
        self.fields['request_log_id'].required = True
        
    #Meta class 
    class Meta:
        
        #Model
        model = TaxiOrder 
        
        #Fields 
        fields = ['order_number', 'confirmation_number', 'request_log_id']