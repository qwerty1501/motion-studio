from django.db import models

class Review(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to ='image/client')
    name_ru = models.CharField(verbose_name='Полное имя', max_length=50, blank=True, null=True)
    name_en = models.CharField(verbose_name='Full name', max_length=50)
    title_ru = models.TextField(verbose_name='Описание', blank=True, null=True)
    title_en = models.TextField(verbose_name='Description')
    
    class Meta:
        verbose_name = 'Отзыв клиента'
        verbose_name_plural = 'Отзывы клиентов'
    
    
class ClientVideo(models.Model):
    video = models.URLField(verbose_name='URL видео', max_length=200)
    title_ru = models.TextField(verbose_name='Описание', blank=True, null=True)
    title_en = models.TextField(verbose_name='Description')
    
    class Meta:
        verbose_name = 'Видео клиента'
        verbose_name_plural = 'Видео клиента'