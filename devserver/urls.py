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
from django.contrib import admin
from django.views import generic
from django.urls import path, include
from django.contrib.auth.mixins import LoginRequiredMixin

# Home view
class Home(LoginRequiredMixin, generic.TemplateView):

    # Template
    template_name = 'devserver/home.html'


urlpatterns = [
    path('admin/', admin.site.urls),

    # Home url
    path('', Home.as_view(), name='home'),

    # Admin dashboard
    path('admin_dashboard/', include('admin_dashboard.urls', namespace='admin_dashboard')),

    # Accounts URLS
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # File upload
    path('file_upload/', include('file_upload.urls', namespace='file_upload')),

    # File download
    path('file_download/', include('file_download.urls', namespace='file_download')),

    # Taxi Log
    path('taxi_log/', include('taxi_log.urls', namespace='taxi_log')),
]
