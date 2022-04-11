from django.contrib import admin
from .models import Notes
from groups.models import NotesGroups

# Register your models here.

from ckeditor.widgets import CKEditorWidget
from django import forms
class NotesAdminForm(forms.ModelForm):
    full_text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Notes
        fields = '__all__'

class NotesAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)
  form = NotesAdminForm

class NotesGroupsAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)

admin.site.register(Notes, NotesAdmin)
admin.site.register(NotesGroups, NotesGroupsAdmin)