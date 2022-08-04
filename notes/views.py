from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm, NoteEditForm
from django.utils import timezone

# Create your views here.

def view_notes(request):
    notes = Notes.objects.filter(note_owner=request.user).order_by('date_create', 'date_update')
    data = {
    "title": "Notes",
    "heading": "Мои заметки",
    'notes': notes
    }
    return render(request, 'notes/notes.html', data)

def add_note(request):
    post_form= NoteEditForm(request.POST)
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            newnote = form.save(commit=False)
            newnote.note_owner = request.user
            newnote.save()
            return redirect('notes:view_notes')
        else:
            error = "Форма заполнена неверно"

    form = NotesForm()

    data = {"title": "New note",
            "heading": "Добавление новой заметки",
            'form': form,
            'error': error,
            'post_form' : post_form,}

    return render(request, 'notes/note_edit.html', data)

def detail(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    data = {
    "title": "Note",
    "heading": f'{note.group_name} - {note.title}',
    'note': note,
    }
    return render(request, 'notes/note.html', data)

def edit_note(request, note_id):
    post_form= NoteEditForm(request.POST)
    note = get_object_or_404(Notes, pk=note_id)
    error = ''
    # Обработка метода GET
    if request.method == 'GET':
        form = NotesForm(instance=note)
        data = {"title": "Update note",
                "heading": f"Изменение заметки - {note.title}",
                'note': note,
                'form': form,
                'error': error,
                'post_form' : post_form,
                }
        return render(request, 'notes/note_edit.html', data)
    # Обработка метода POST
    else:
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            note.date_update = timezone.now()
            editnote = form.save(commit=False)
            editnote.note_owner = request.user
            editnote.save()
            return redirect('notes:detail', note_id)
        else:
            error = "Форма заполнена неверно"

def delete_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    note.delete()
    #return redirect('notes:view_notes')
    return redirect('groups:view_groups')
    #return HttpResponseRedirect(notes_url)
