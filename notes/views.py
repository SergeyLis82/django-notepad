from django.shortcuts import render
from .models import Notes

# Create your views here.

def notes(request):
    notes = Notes.objects.order_by('-date')
    return render(request, 'notes/notes.html', {'notes': notes})