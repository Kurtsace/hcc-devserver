"""devserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'admin_dashboard'

urlpatterns = [
    path('', staff_member_required( views.AdminDashboard.as_view() ), name='admin_dashboard_view'),
    path('details/<str:username>/all_orders/', staff_member_required( views.UserTaxiOrderList.as_view() ), name='user_order_list_view')
]
