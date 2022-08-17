from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Notes(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    preview = models.CharField('Превью', max_length=250)
    full_text = RichTextField('Текст', blank=True, null=True)
    important = models.BooleanField(default=False, verbose_name="Важно")
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', null=True, blank=True)
    group_name = models.ForeignKey('groups.NotesGroups', on_delete=models.SET_DEFAULT, default=1, verbose_name="Группа")
    note_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="Владелец")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
