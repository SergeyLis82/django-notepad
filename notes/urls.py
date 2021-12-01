from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes, name='notes'),
    path('add_note', views.add_note, name='add_note'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('<int:note_id>/edit/', views.update_note, name='update_note'),
]