from . import views 
from django.urls import path

app_name = 'taxi_log'

urlpatterns = [
    path('', views.TaxiOrderList.as_view(), name='order_list_view'),
    path('order/', views.CreateOrder.as_view(), name='create_order'),
]