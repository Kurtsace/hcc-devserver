from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.

#Taxi order class
class TaxiOrder(models.Model):
    
    #Request log id
    request_log_id = models.PositiveIntegerField(blank=False, null=True)
    
    #Auto generated order number 
    order_number = models.PositiveIntegerField(null=False, blank=False)

    #Confirmation number
    confirmation_number = models.PositiveIntegerField(null=True, blank=False)
    
    #Date created 
    date_created = models.DateTimeField(auto_now_add=True)

    #User who created this order
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Redirect
    def get_absolute_url(self):
        return reverse('taxi_log:order_list_view')
    
    #Str 
    def __str__(self):
        return str( self.order_number )