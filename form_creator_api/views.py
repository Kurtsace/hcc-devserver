from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewLocationForm

#Import model
from .models import SafewayLocation, RequestLogURL

# Create your views here.

# API Home view 
class APIHomeView(LoginRequiredMixin, generic.TemplateView):
    
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
        return reverse('form_creator_api:api_home_view')
    
# Update Request Log URL
class UpdateRequestLogURL(LoginRequiredMixin, generic.UpdateView):
    
    # Template 
    template_name = 'form_creator_api/update_request_log_url.html'
    
    # Model 
    model = RequestLogURL
    
    # Fields 
    fields = ['url']