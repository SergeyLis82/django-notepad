from django.shortcuts import render, redirect, get_object_or_404
from ..models import NotesGroups
from ..forms import NotesGroupsForms
from django.utils import timezone

def view_groups(request):
    groups = NotesGroups.objects.order_by('-date_create')
    data = {
    "title": "Groups",
    "heading": "Мои группы",
    'groups': groups
    }
    return render(request, 'notes/groups.html', data)

def detail(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
    data = {
    "title": "Group",
    "heading": f'{group.groupname}',
    'group': group,
    }
    return render(request, 'notes/group.html', data)

def add_group(request):
    error = ''
    if request.method == 'POST':
        form = NotesGroupsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:view_groups')
        else:
            error = "Форма заполнена неверно"

    form = NotesGroupsForms()

    data = {"title": "New note",
            "heading": "Добавление новой группы",
            'form': form,
            'error': error}

    return render(request, 'notes/group_edit.html', data)

def edit_group(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
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
        return render(request, 'notes/group_edit.html', data)
    # Обработка метода POST
    else:
        form = NotesGroupsForms(request.POST, instance=group)
        if form.is_valid():
            group.date_update = timezone.now()
            form.save()
            return redirect('notes:view_groups')
        else:
            error = "Форма заполнена неверно"

def delete_group(request, group_id):
    group = get_object_or_404(NotesGroups, pk=group_id)
    group.delete()
    return redirect('notes:view_groups')
