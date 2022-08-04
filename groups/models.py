from django.db import models
from django.contrib.auth.models import User
from notes.models import Notes

# Create your models here.
class NotesGroups(models.Model):
    groupname = models.CharField('Имя группы', max_length=100)
    groupdescription = models.TextField('Описание группы')
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', null=True, blank=True)
    group_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name="Владелец")
    
    def __str__(self):
        return self.groupname
    
    def calculateNotes(self):
        return Notes.objects.filter(group_name=self).count()
    
    calculateNotes.short_description = 'Количество заметок'
    
    countNotes = property(calculateNotes)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'