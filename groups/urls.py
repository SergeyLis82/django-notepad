from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', view_groups, name='view_groups'),
    path('<int:group_id>/', detail, name='group_detail'),
    path('add_group/', add_group, name='add_group'),
    path('<int:group_id>/edit/', edit_group, name='edit_group'),
    path('<int:group_id>/delete/', delete_group, name='delete_group'),
]