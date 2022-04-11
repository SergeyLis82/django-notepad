from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Notes(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    preview = models.CharField('Превью', max_length=250)
    full_text = RichTextField('Текст', blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', null=True, blank=True)
    group_name = models.ForeignKey('groups.NotesGroups', on_delete=models.SET_DEFAULT, default=4, verbose_name="Группа")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
