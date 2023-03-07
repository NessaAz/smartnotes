from django.shortcuts import render

from .models import *

def list(request):
    all_notes = Notes.objects.all()
    
    return render(request, 'notes/note_list.html',
                  {
                      'notes' : all_notes,
                  }
                  )
    
    