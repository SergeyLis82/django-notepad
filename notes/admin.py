from django.contrib import admin
from .models import Notes
from groups.models import NotesGroups

# Register your models here.

from ckeditor.widgets import CKEditorWidget
from django import forms

# Добавление ckeditor в форму создания/редактирования заметки
class NotesAdminForm(forms.ModelForm):
    full_text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Notes
        fields = '__all__'

# Регистрация моделей в админке сайта
class NotesAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)
  form = NotesAdminForm
  list_display = ("title", "preview", "group_name", "date_create", "date_update", "note_owner", "important")
  list_filter = ("group_name",)

class NotesGroupsAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)
  list_display = ("groupname", "groupdescription", "group_owner", "countNotes", "date_create", "date_update")

admin.site.register(Notes, NotesAdmin)
admin.site.register(NotesGroups, NotesGroupsAdmin)