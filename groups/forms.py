from .models import NotesGroups
from django.forms import ModelForm, TextInput

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