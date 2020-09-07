from .models import File 
import os

#Pre save signal 
def pre_save_file(sender, instance, *args, **kwargs):
    
    #Make sure model exists in the DB 
    if instance.pk: 
        
        #Get the old path to the file 
        old_filepath = sender.objects.get(pk=instance.pk).uploaded_file.path
        
        #Set a new file path 
        new_filepath = instance.uploaded_file.path
        
        #If the file paths differ, remove the old file 
        if old_filepath != new_filepath:
            
            #Delete the file 
            if os.path.exists(old_filepath):
                os.remove(old_filepath)


#Pre delete signal 
def delete_linked_file(sender, instance, *args, **kwargs):
    
    #Path to file 
    filepath = instance.uploaded_file.path
    
    #Delete the associated file using its path 
    if( os.path.exists(filepath) ):
        os.remove(filepath)
