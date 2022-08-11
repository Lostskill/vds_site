from django.db import models
from django.urls import reverse

class VideoCard(models.Model):
    name = models.CharField(max_length= 100, )
    manufacturer = models.CharField(max_length= 20)
    chip = models.CharField(max_length=100)
    price = models.FloatField()
    video_memory = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    amount = models.FloatField(null=True)
    rub_key = models.ForeignKey('Rub', null=True, on_delete = models.PROTECT, verbose_name="Тип Видеокарты")
    image = models.ImageField(null=True,blank=True)
    slug = models.SlugField(max_length=255,null=True,  db_index=True, verbose_name="URL")   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vcard', kwargs= {'card_slug': self.slug})

    class Meta:
        index_together = (('id','slug'),)
        verbose_name = 'ВидеоКарта'
        verbose_name_plural = 'Видеокарты'


class Rub(models.Model):
    name = models.CharField(max_length=20, db_index = True, verbose_name = 'название')
    slug_field = models.SlugField(max_length=255, null=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubrics', kwargs= {'cat_slug': self.slug_field})
    
    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    
