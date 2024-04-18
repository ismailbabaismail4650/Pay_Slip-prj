from django.shortcuts import render
from. models import Staff, Pay_slip
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.

def home (request):
    staff = Staff.objects.all()
    context = {
       'staffs':staff
    }
    return render(request,'base/home.html', context)
    
def pay_slip (request, pk):
    staff = Staff.objects.get(id = pk)
    template_path = 'base/pay_slip.html'
    paySlip = Pay_slip.objects.get(position = staff.id)
    
    context= {
            'staff':staff,
            'paySlip':paySlip

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

     

