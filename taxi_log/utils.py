from django.http import HttpResponse
from django.template.loader import get_template

from io import BytesIO

from xhtml2pdf import pisa 



#Render html template into pdf
def render_to_pdf(template_name, context_dict={}):
    
    #Get the template 
    template = get_template(template_name)
    
    #Load the context dict
    html = template.render(context_dict)
    
    #Encode the contents into a file
    file = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), file)
    
    #Return the file as an http response if no errors are found 
    if not pdf.err:
        return HttpResponse(file.getvalue(), content_type='application/pdf')
    else:
        return None