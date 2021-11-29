from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm

# Create your views here.

def notes(request):
    notes = Notes.objects.order_by('-date')
    data = {
    "title": "Notes",
    "heading": "Мои заметки",
    'notes': notes
    }
    return render(request, 'notes/notes.html', data)

def add_note(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
        else:
            error = "Форма заполнена неверно"

    form = NotesForm()

    data = {"title": "New note",
            "heading": "Добавление новой заметки",
            'form': form,
            'error': error}

    return render(request, 'notes/add_note.html', data)