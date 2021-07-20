from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    #Класс категорий статей
    #
    title = models.CharField(verbose_name='Название', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.title



class Tag(models.Model):
    #Класс тегов статей
    #
    title = models.CharField(verbose_name='Тег', max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title

class News(models.Model):
    #Класс новостей
    #
    user = models.ForeignKey(           #у одного автора может много статей
        User,                           #у каждой статьи есть автор
        verbose_name='Автор',
        on_delete=models.CASCADE,       #при удалении автора, все статьи удаляются
        )
    category = models.ForeignKey(       #в одной категории может быть много статей
        Category,                       #связь категории со списком категорий
        verbose_name='Категория',
        on_delete=models.SET_NULL,      #при удалении категории удалится только категория, но статьи останутся
        null=True                       #поле категории в статье может быть пустое
    )
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    text_min = models.TextField(verbose_name='Анонс', max_length=300)
    text = models.TextField(verbose_name='Текст статьи')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    description = models.CharField(verbose_name='Описание', max_length=100)
    keywords = models.CharField(verbose_name='Ключевые слова', max_length=50)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
