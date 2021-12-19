from django.db import models

class Books(models.Model):
    title = models.CharField('Название', max_length=250)
    task = models.TextField('Описание')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
