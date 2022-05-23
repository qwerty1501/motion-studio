from django.db import models


class FeedbackLink(models.Model):
    name_ru = models.CharField(
        verbose_name='Имя',
        max_length=30,
        blank=True, null=True
    )
    name_en = models.CharField(
        verbose_name='Name',
        max_length=30
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        blank=True,
        null=True
    )
    budget = models.CharField(
        verbose_name='Бюджет',
        max_length=50
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=30,
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        blank=True,
    )

    def __str__(self):
        return self.name_en
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        
        
class OurClient(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to ='image/client'
        )
    name_ru = models.CharField(
        verbose_name='Полное имя',
        max_length=50,
        blank=True, null=True
        )
    title_ru = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
        )
    name_en = models.CharField(
        verbose_name='Full name',
        max_length=50
        )
    title_en = models.TextField(
        verbose_name='Description'
        )
    
    class Meta:
        verbose_name = 'Наш клиент'
        verbose_name_plural = 'Нашы клиенты'