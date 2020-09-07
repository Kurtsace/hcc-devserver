from django.forms import ModelForm, FileField, ValidationError, HiddenInput
from django.forms.widgets import FileInput
from .models import File

# Form to upload a file and create a new model
class UploadFileForm(ModelForm):

    class Meta:

        # Model
        model = File

        # Fields
        fields = ('uploaded_file', 'description', 'version', 'user')

        # Widgets
        widgets = {
            'uploaded_file': FileInput(),
            'user' : HiddenInput(),
        }

    # Clean the file field
    def clean_uploaded_file(self):

        # Get the file and validate it
        file = self.cleaned_data['uploaded_file']

        # File extension
        ext = file.name.split('.')[-1].lower()
        print(ext)

        # Allowed file types
        allowed_types = ['exe', 'rar', 'zip']

        # Make sure the file is an exe
        if ext not in allowed_types:
            raise ValidationError(
                'This is not a supported file type. Supported file types: exe, rar, zip')

        return file
    
    #Update the file 
class UpdateFileForm(ModelForm):

    class Meta:

        # Model
        model = File

        # Fields
        fields = ('uploaded_file', 'version')

        # Widgets
        widgets = {
            'uploaded_file': FileInput()
        }

    # Clean the file field
    def clean_uploaded_file(self):

        # Get the file and validate it
        file = self.cleaned_data['uploaded_file']

        # File extension
        ext = file.name.split('.')[-1].lower()

        # Allowed file types
        allowed_types = ['exe', 'rar', 'zip']

        # Make sure the file is an exe
        if ext not in allowed_types:
            raise ValidationError(
                'This is not a supported file type. Supported file types: exe, rar, zip')

        return file