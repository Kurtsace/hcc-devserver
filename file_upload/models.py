from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, pre_save

import ntpath

# Create your models here.

#User directory path 
def user_directory_path(instance, filename):
    return 'uploads/{}'.format(filename)

#File model for uploaded files 
class File(models.Model):
    
    #File 
    uploaded_file = models.FileField(upload_to=user_directory_path, blank=False, null=False)
    
    #Filename 
    file_name = models.CharField(max_length=255, blank=True, null=True)
    
    #Version 
    version = models.CharField(max_length=255, blank=True, null=True)

    #Slug field 
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    
    #Description 
    description = models.TextField(blank=False, null=False)
    
    #Upload date 
    upload_date = models.DateTimeField(auto_now_add=True)
    
    #User who uploaded the file 
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    
    #Override save method 
    def save(self, *args, **kwargs):
        
        #If this model entry does not exist yet
        if not self.pk:
            
            #Set the file name --split the file path and get the file name 
            self.file_name = ntpath.basename(self.uploaded_file.name).split('.')[0]
            
        #Set the slug of the file --set to format FILE-NAME-VERSION
        #ex: file-name-1-23-4
        text = self.file_name + '-' + self.version
        self.slug = slugify(text)
        
        #Call super save method 
        super(File, self).save(*args, **kwargs)
        
    #Absoulte URL 
    def get_absolute_url(self):
        return reverse_lazy('file_upload:file_detail', kwargs={'slug' : self.slug})
        
    
    #str representation
    def __str__(self):
        return self.file_name



#Connect signals 
from .signals import pre_save_file, delete_linked_file

#Connect pre save
pre_save.connect(pre_save_file, sender=File)

#Connect pre delete
pre_delete.connect(delete_linked_file, sender=File)