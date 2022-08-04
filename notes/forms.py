from .models import Notes
from groups.models import NotesGroups
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField, Form, CharField
from ckeditor.widgets import CKEditorWidget

class NoteEditForm(Form):
    full_text = CharField(widget=CKEditorWidget, label='')

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        group_name = ModelChoiceField(queryset=NotesGroups.objects.all(), empty_label=None, to_field_name="groupname")
        fields = ['group_name', 'title', 'preview', 'important', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control'})
        }
