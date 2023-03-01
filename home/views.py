from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'home/welcome.html',
                  {
                      'today': datetime.today()
                  })
    #{} passes info from view to template
    
