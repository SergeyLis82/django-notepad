from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'preview', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Заголовок",
                'class': 'form-control'
            }),
            'preview': TextInput(attrs={
                'placeholder': "Превью",
                'class': 'form-control'
            }),
            'date': DateTimeInput(attrs={
                'type': 'datetime',
                'placeholder': "Дата и Время создания",
                'class': 'form-control'
            }),
            'full_text': Textarea(attrs={
                'placeholder': "Текст",
                'class': 'form-control'})
        }