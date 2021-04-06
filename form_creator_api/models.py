from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse 

# Create your models here

# Safeway location model 
class SafewayLocation(models.Model):
    
    # Location name 
    location_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    # Fax number 
    # TODO --Might need a more specialized external phone library to validate
    # but it shouldnt matter for now (?), will see how user testing goes
    fax_number = models.CharField(max_length=255, blank=False, null=False, unique=True)
    
    #  User who made this 
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('form_creator_api:api_home_view')
    
    # String representation 
    def __str__(self):
        return self.location_name
    
# Request Log URL model
# Singleton model, should only have 1 instance ever 
class RequestLogURL(models.Model):
    
    # URL 
    url = models.CharField(max_length=400, blank=False, null=False, unique=True)
    
    # User who made this 
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    
    # Override save method 
    def save(self, *args, **kwargs):
        
        # Ensure the pk does not exist for the object we want to add
        # and object exist in the database 
        if not self.pk and RequestLogURL.objects.exists():
            
            # Raise a validation error 
            raise ValidationError("Only one instance of this model is allowed!")
        
        # Call super save method 
        return super(RequestLogURL, self).save(*args, **kwargs)
    
    # Redirect
    def get_absolute_url(self):
        return reverse('form_creator_api:api_home_view')
    
    # String representation 
    def __str__(self):
        return self.url
        
