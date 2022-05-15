from unicodedata import name
from django.db import models

# Create your models here.


class VideoCard(models.Model):
    name = models.CharField(max_length= 100, )
    manufacturer = models.CharField(max_length= 20)
    chip = models.CharField(max_length=100,)
    price = models.FloatField(null=True, blank=True)
    video_memory = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    amount = models.FloatField(null=True)
    rub_key = models.ForeignKey('Rub', null=True, on_delete = models.PROTECT, verbose_name="Тип Видеокарты")

    class Meta:
        verbose_name = 'ВидеоКарта'
        verbose_name_plural = 'ВидеоКарты'

class Rub(models.Model):
    name = models.CharField(max_length=20, db_index = True, verbose_name = 'название')

    def __str__(self):
        return self.name