from django.shortcuts import render, redirect, get_object_or_404
from .models import NotesGroups
from .forms import NotesGroupsForms
from notes.models import Notes
from django.utils import timezone

def view_groups(request):
    try:
        groups = NotesGroups.objects.filter(group_owner=request.user).order_by('-date_create')
        data = {
        "title": "Groups",
        "heading": "Мои группы",
        'groups': groups,
        }
        return render(request, 'groups/groups.html', data)
    except TypeError:
        data = {
        "title": "Groups",
        "heading": "Not found",
        "content": "Необходимо войти или зарегистрироваться"
        }
        return render(request, 'main/index.html', data)

def view_group_notes(request, group_id):
    notes = Notes.objects.filter(group_name=group_id).order_by('date_create', 'date_update')
    data = {
    "title": "Notes",
    "heading": "Мои заметки",
    'notes': notes
    }
    return render(request, 'notes/notes.html', data)

def detail(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
    if group.group_owner == request.user:
        data = {
        "title": "Group",
        "heading": f'{group.groupname}',
        'group': group,
        }
        return render(request, 'groups/group.html', data)
    else:
        data = {
        "title": "Group",
        "heading": "Not found",
        }
        return render(request, 'groups/group.html', data)

def add_group(request):
    error = ''
    if request.method == 'POST':
        form = NotesGroupsForms(request.POST)
        if form.is_valid():
            newgroup = form.save(commit=False)
            newgroup.group_owner = request.user
            newgroup.save()
            return redirect('groups:view_groups')
        else:
            error = "Форма заполнена неверно"

    form = NotesGroupsForms()

    data = {"title": "New note",
            "heading": "Добавление новой группы",
            'form': form,
            'error': error}

    return render(request, 'groups/group_edit.html', data)

def edit_group(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
    if group.group_owner == request.user:
        error = ''
        # Обработка метода GET
        if request.method == 'GET':
            form = NotesGroupsForms(instance=group)
            data = {"title": "Update note",
                    "heading": f"Изменение группы - {group.groupname}",
                    'group': group,
                    'form': form,
                    'error': error
                    }
            return render(request, 'groups/group_edit.html', data)
        # Обработка метода POST
        else:
            form = NotesGroupsForms(request.POST, instance=group)
            if form.is_valid():
                group.date_update = timezone.now()
                editgroup = form.save(commit=False)
                editgroup.group_owner = request.user
                editgroup.save()
                return redirect('groups:view_groups')
            else:
                error = "Форма заполнена неверно"
    else:
        data = {
                "title": "Group",
                "heading": "Not found",
                }
        return render(request, 'groups/group.html', data)

def delete_group(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
    if group.group_owner == request.user:
        group.delete()
        return redirect('groups:view_groups')
    else:
        data = {
                "title": "Group",
                "heading": "Not found",
                }
        return render(request, 'groups/group.html', data)
