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