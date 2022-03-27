from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.view_notes, name='view_notes'),
    path('add_note/', views.add_note, name='add_note'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('<int:note_id>/delete/', views.delete_note, name='delete_note'),
]