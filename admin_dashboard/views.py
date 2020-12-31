from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from taxi_log.filters import TaxiOrderFilter
from taxi_log.models import TaxiOrder

from django.contrib.auth import get_user_model


# Create your views here.

#Main dashboard view 
class AdminDashboard(LoginRequiredMixin, generic.TemplateView):
    
    #Template 
    template_name = 'admin_dashboard/admin_dashboard_view.html'
    
    #Context dict
    def get_context_data(self, **kwargs):
        
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        #Filter 
        order_filter = TaxiOrderFilter(self.request.GET, queryset=TaxiOrder.objects.all())
        taxiorder_list = order_filter.qs
        
        #User list
        user_list = get_user_model().objects.all()
        
        #Set context data
        context['order_filter'] = order_filter
        context['taxiorder_list'] = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False)
        context['user_list'] = user_list
        
        return context
    
class UserTaxiOrderList(LoginRequiredMixin, generic.ListView):
    
    #Template
    template_name = 'admin_dashboard/user_order_list.html'
    
    def get_context_data(self, **kwargs):
        
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        
        #Set context data
        context['username'] = self.kwargs['username']
        
        return context
    
    #Queryset 
    def get_queryset(self):
        
        #Query all user orders 
        query = get_object_or_404(get_user_model(), username=self.kwargs['username']).taxiorder_set.filter(request_log_id__isnull=False, confirmation_number__isnull=False)
        
        return query
        
