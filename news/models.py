from django.db import models
from django.contrib.auth.models import User

class DoramaNews(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    dorama_name = models.CharField(max_length=100, verbose_name="Название дорамы")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Автор")
    likes = models.ManyToManyField(User, related_name='dorama_likes', blank=True, verbose_name="Лайки")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость дорамы"
        verbose_name_plural = "Новости дорам"


class Comment(models.Model):
    post = models.ForeignKey(DoramaNews, related_name="comments", on_delete=models.CASCADE, verbose_name="Пост")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    body = models.TextField(verbose_name="Текст комментария")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f'{self.post.dorama_name} - {self.author.username}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class DoramaVideo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название видео")
    video_file = models.FileField(upload_to='videos/', verbose_name="Загрузить видео файл", null=True, blank=True)
    video_url = models.URLField(verbose_name="Или ссылка на YouTube", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"