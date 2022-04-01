from django.urls import path
from .views import views_notes

app_name = 'notes'

urlpatterns = [
    path('', views_notes.view_notes, name='view_notes'),
    path('add_note/', views_notes.add_note, name='add_note'),
    path('<int:note_id>/', views_notes.detail, name='detail'),
    path('<int:note_id>/edit/', views_notes.edit_note, name='edit_note'),
    path('<int:note_id>/delete/', views_notes.delete_note, name='delete_note'),
]