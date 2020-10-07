from django.shortcuts import render
from django.views import generic 

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TaxiOrder
from .forms import OrderForm

from django.utils import timezone

from .utils import render_to_pdf

# Create your views here.


#Create order view
class CreateOrder(LoginRequiredMixin, generic.UpdateView):
    
    #Template
    template_name = 'taxi_log/create_order_form.html'

    #Form 
    form_class = OrderForm

    #Get the object to update
    def get_object(self):
        
        #Query a set of objects from today 
        current_date = timezone.now().date()
        queryset = TaxiOrder.objects.filter(date_created__date=current_date)
        
        #If the quesryset is empty, initialize a new object 
        if not queryset:
            
            #Create an entry 
            order_number = int( timezone.now().strftime('%m%d') ) * 1000
            order = TaxiOrder(order_number=order_number, user=self.request.user)
            
            #Save the instance
            order.save()
            
            #Return the object
            return order
        
        #If object(s) already exists
        else:
            
            #Create an order and increment the order number from the previous entry
            order_number = str(queryset.last().order_number)
            
            #Split the order number and increment only the digits after the date
            #This will prevent still having the same date that will eventually increment to the point that the
            #entire order number will auto increment into the next date
            lhs_order_number = order_number[:4]
            print(lhs_order_number)
            rhs_order_number = '%03d' % ( int(order_number[4:]) + 1 )
            print(rhs_order_number)
            
            order_number = int( lhs_order_number + rhs_order_number )
            
            order = TaxiOrder(order_number=order_number, user=self.request.user)
            
            #Save the instance 
            order.save()

            #Return the object
            return order




#Order list view 
class TaxiOrderList(LoginRequiredMixin, generic.ListView):
    
    #Template
    template_name = 'taxi_log/order_list_view.html'
    
    def get_queryset(self):
        
        #Query for objects from today with non null entries
        current_date = timezone.now().date()
        query = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=current_date)
        
        return query


    
#View current query as PDF
class TaxiOrderListPDF(LoginRequiredMixin, generic.ListView):
    
    #Query
    def get_queryset(self):
        
        #Query for objects from today with non null entries
        current_date = timezone.now().date()
        query = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=current_date)
        
        return query
    
    #Get request to view the PDF
    def get(self, request, *args, **kwargs):
        
        #PDF html template 
        template_name = 'taxi_log/order_list_pdf.html'
        
        #Context dictionary 
        context_dict = {'taxiorder_list' : self.get_queryset}
        
        #Generate a pdf file for the query 
        pdf = render_to_pdf(template_name, context_dict)
        
        #Return the response 
        return pdf
    
#Download current query as a pdf
class TaxiOrderListPDFDownload(LoginRequiredMixin, generic.ListView):
    
    #Query
    def get_queryset(self):
        
        #Query for objects from today with non null entries
        current_date = timezone.now().date()
        query = TaxiOrder.objects.filter(request_log_id__isnull=False, confirmation_number__isnull=False, date_created__date=current_date)
        
        return query
    
     #Get request to view the PDF
    def get(self, request, *args, **kwargs):
        
        #PDF html template 
        template_name = 'taxi_log/order_list_pdf.html'
        
        #Context dictionary 
        context_dict = {'taxiorder_list' : self.get_queryset}
        
        #Generate a pdf file for the query 
        pdf = render_to_pdf(template_name, context_dict)
        
        #Filename of the pdf --Formatted as "Taxi_Log_DATE.pdf"
        current_date = timezone.now().date()
        filename = 'Taxi_Log_{}.pdf'.format(current_date)
        
        #Set content disposition
        content = 'attachment; filename={}'.format(filename)
        pdf['Content-Disposition'] = content
        
        #Return the response 
        return pdf