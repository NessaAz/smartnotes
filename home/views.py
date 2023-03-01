from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/welcome.html',
                  {
                      'today': datetime.today()
                  })
    #{} passes info from view to template
    

@login_required
def authorized(request):
    return render(request, 'home/authorized.html',{})