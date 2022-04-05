from .models import Notes, NotesGroups
from django.forms import ChoiceField, ModelForm, TextInput, DateTimeInput, Textarea, ModelChoiceField

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        group_name = ModelChoiceField(queryset=NotesGroups.objects.all(), empty_label=None, to_field_name="groupname")
        fields = ['group_name', 'title', 'preview', 'full_text']

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
        
class NotesGroupsForms(ModelForm):
    class Meta:
        model = NotesGroups
        fields = ['groupname', 'groupdescription']
        widgets = {
            'groupname': TextInput(attrs={
                'class': 'form-control'
            }),
            'groupdescription': TextInput(attrs={
                'class': 'form-control'
            }),
        }