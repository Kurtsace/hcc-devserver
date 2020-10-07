import django_filters
from django.forms import DateInput

from .models import TaxiOrder

#Filter class for querying
class TaxiOrderFilter(django_filters.FilterSet):
    
    class Meta: 
        
        #Model
        model = TaxiOrder
        
        #Fields
        fields = ['date_created']
        
    #Date filter
    date_created = django_filters.DateFilter(label='Date Created', lookup_expr='date', widget=DateInput(attrs={'type': 'date'}))