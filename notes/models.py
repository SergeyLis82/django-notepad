from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    preview = models.CharField('Превью', max_length=250)
    full_text = models.TextField('Текст')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', null=True, blank=True)
    group_id = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

class NotesGroups(models.Model):
    groupname = models.CharField('Имя группы', max_length=100)
    groupdescription = models.TextField('Описание группы')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', null=True, blank=True)
    
    def __str__(self):
        return self.groupname
    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'