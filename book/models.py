from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class PostBook(models.Model):
    objects = None
    category_book = {
        'драма': 'драма',
        'комедия': 'комедия',
        'хоррор': 'хоррор',
        'сказка': 'сказка'
    }


    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    image = models.ImageField(upload_to='images/', verbose_name='Укажите фото', blank=True)
    descript = models.TextField(verbose_name='Описание')
    music = models.FileField(upload_to='audio/', verbose_name='Аудио озвучка', blank=True)
    video = models.URLField(verbose_name='Укажите ссылку на видео', blank=True)
    category = models.CharField(max_length=100, choices=category_book, verbose_name='Категория')
    review = models.TextField(verbose_name='Отзыв специалиста')
    pages = models.PositiveIntegerField(verbose_name='Сколько страниц')
    time_book = models.PositiveIntegerField(verbose_name='укажите время новости')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_at}'

    class Meta:
        verbose_name = 'добавить книгу'
        verbose_name_plural = 'список книг'

class Review(models.Model):
    what = models.ForeignKey(PostBook, on_delete=models.CASCADE,
                             related_name='review_book')
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.what} - {self.stars}'