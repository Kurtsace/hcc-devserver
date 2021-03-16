from django.shortcuts import render
from django.views import generic 

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TaxiOrder
from .forms import OrderForm

from django.utils import timezone

from .utils import render_to_pdf

from .filters import TaxiOrderFilter

# Create your views here.
old_obj = None

#Create order view
class CreateOrder(LoginRequiredMixin, generic.UpdateView):
    
    #Template
    template_name = 'taxi_log/create_order_form.html'

    #Form 
    form_class = OrderForm
    #fields = ['order_number', 'confirmation_number', 'request_log_id']
    
    # Model 
    model = TaxiOrder
    
    # GET method override 
    def get(self, request, *args, **kwargs):
        
        # Set object 
        self.object = self.get_object()
        
        # Set form and form class
        form_class = self.get_form_class()
        form = self.get_form()
        return self.render_to_response( self.get_context_data(form = form) )
    
    # POST method override
    def post(self, request, *args, **kwargs):
        
        # Set the form and form class
        self.object = TaxiOrder.objects.filter(date_created__date=timezone.now().date()).last()
        form_class = self.get_form_class()
        form = self.get_form()
        
        # Validate the forms 
        if(form.is_valid()):
            return self.form_valid(form)
        
        return self.form_invalid(form)
        

    #Get the object to update
    def get_object(self):
        
        #Query a set of objects from today 
        current_date = timezone.now().date()
        queryset = TaxiOrder.objects.filter(date_created__date=current_date)
        
        #If the queryset is empty, initialize a new object 
        if not queryset:
            
            #Create an entry 
            order_number = int( timezone.now().strftime('%m%d') ) * 1000
            order = TaxiOrder(order_number=order_number, user=self.request.user)
            
            #Save the instance
            order.save()
        
        #If object(s) already exists
        else:
            
            #Create an order and increment the order number from the previous entry
            order_number = str(queryset.last().order_number)
            
            #Split the order number and increment only the digits after the date
            #This will prevent still having the same date that will eventually increment to the point that the
            #entire order number will auto increment into the next date
            date = timezone.now().strftime('%m%d')
            lhs_order_number = order_number[:len(date)-1]
            print(lhs_order_number)
            rhs_order_number = '%04d' % ( int(order_number[len(date)-1:]) + 1 )
            
            order_number = int( lhs_order_number + rhs_order_number )
            
            # Create an order 
            order = TaxiOrder(order_number=order_number, user=self.request.user)
                
            # Save the instance 
            order.save()
            
        return order


#Order list view 
class TaxiOrderList(LoginRequiredMixin, generic.ListView):
    
    #Template
    template_name = 'taxi_log/order_list_view.html'
    
    #Context dict
    def get_context_data(self, **kwargs):
        
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        #Filter 
        order_filter = TaxiOrderFilter(self.request.GET, queryset=TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False))
        
        if self.request.GET.get('date_created'):
            taxiorder_list = order_filter.qs#.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=timezone.now().date())
        else:
            taxiorder_list = order_filter.qs.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=timezone.now().date())
        
        #Context variables
        queried_date = self.request.GET.get('date_created')
        
        #Set context data
        context['order_filter'] = order_filter
        context['taxiorder_list'] = taxiorder_list
        context['queried_date'] = queried_date if queried_date else timezone.now().date() 
        
        return context
    
    def get_queryset(self):
        
        #Query for objects from today with non null entries
        current_date = timezone.now().date()
        query = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=current_date)
        
        return query


    
#View current query as PDF
class TaxiOrderListPDF(LoginRequiredMixin, generic.View):
    
    #Get request to view the PDF
    def get(self, request, *args, **kwargs):
        
        #PDF html template 
        template_name = 'taxi_log/order_list_pdf.html'
        
        #Query date 
        query_date = self.kwargs['date'] if self.kwargs['date'] else timezone.now().date()
        
        #Query set 
        taxiorder_list = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=query_date)
        
        #Context dictionary 
        context_dict = {'taxiorder_list' : taxiorder_list, 'query_date' : query_date}
        
        #Generate a pdf file for the query 
        pdf = render_to_pdf(template_name, context_dict)
        
        #Return the response 
        return pdf



#Download current query as a pdf
class TaxiOrderListPDFDownload(LoginRequiredMixin, generic.View):
    
     #Get request to view the PDF
    def get(self, request, *args, **kwargs):
        
        #PDF html template 
        template_name = 'taxi_log/order_list_pdf.html'
        
        #Query date 
        query_date = self.kwargs['date'] if self.kwargs['date'] else timezone.now().date()
        
        #Query set 
        taxiorder_list = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=query_date)
        
        #Context dictionary 
        context_dict = {'taxiorder_list' : taxiorder_list, 'query_date' : query_date}
        
        #Generate a pdf file for the query 
        pdf = render_to_pdf(template_name, context_dict)
        
        #Filename of the pdf --Formatted as "Taxi_Log_DATE.pdf"
        filename = 'Taxi_Log_{}.pdf'.format(query_date)
        
        #Set content disposition
        content = 'attachment; filename={}'.format(filename)
        pdf['Content-Disposition'] = content
        
        #Return the response 
        return pdf