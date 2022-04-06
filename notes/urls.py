from django.urls import path
from .views import view_notes, add_note, detail, edit_note, delete_note

app_name = 'notes'

urlpatterns = [
    path('', view_notes, name='view_notes'),
    path('add_note/', add_note, name='add_note'),
    path('<int:note_id>/', detail, name='detail'),
    path('<int:note_id>/edit/', edit_note, name='edit_note'),
    path('<int:note_id>/delete/', delete_note, name='delete_note'),
]