from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    preview = models.CharField('Превью', max_length=250)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'